# PsSetLegoNotifyRoutine

- RVA: `0x00785E80`–`0x00785E8E` (길이 `14` bytes)
- VA: `0x0000000140785E80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `14/14` bytes 표시
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
- `0x00785E80` → RVA `0x00FD9F80` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00785E80  48 89 0D F9 40 85 00            mov qword ptr [rip + 0x8540f9], rcx
00785E87  B8 D0 02 00 00                  mov eax, 0x2d0
00785E8C  C3                              ret
00785E8D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsSetLegoNotifyRoutine(__int64 a1)
{
    *(unsigned __int64 *)(v_rip + 8732921) = a1;
    return 720;
}
```

## 5. (Beta) C Style

```c
int64_t PsSetLegoNotifyRoutine(int64_t Arg1)
{
    *(uint64_t *)(v_rip + 0x8540F9) = Arg1;
    return 720;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00785E80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00785E80[BB_00785E80]
  bb_00785E8D[BB_00785E8D]
```
