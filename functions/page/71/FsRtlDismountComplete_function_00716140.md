# FsRtlDismountComplete

- RVA: `0x00716140`–`0x00716154` (길이 `20` bytes)
- VA: `0x0000000140716140`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `20/20` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00716144` → RVA `0x00FC5008` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00716140  85 D2                           test edx, edx
00716142  78 0E                           js 0x140716152
00716144  48 8B 05 BD EE 8A 00            mov rax, qword ptr [rip + 0x8aeebd]
0071614B  F0 FF 80 DC 02 00 00            lock inc dword ptr [rax + 0x2dc]
00716152  C3                              ret
00716153  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlDismountComplete(__int64 a1, int a2)
{
    __int64 result;

    if (!(sign_flag)) {
        result = *(unsigned __int64 *)(v_rip + 9105085);
    }
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlDismountComplete(int64_t Arg1, int32_t Arg2)
{
    int64_t result;

    if (!(sign_flag)) {
        result = *(uint64_t *)(v_rip + 0x8AEEBD);
    }
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00716140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00716140[BB_00716140]
  bb_00716144[BB_00716144]
  bb_00716152[BB_00716152]
  bb_00716153[BB_00716153]
  bb_00716140 -->|branch| bb_00716152
  bb_00716140 -->|fallthrough| bb_00716144
  bb_00716144 -->|flow| bb_00716152
```
