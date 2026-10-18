# ExecuteHotpatchTestBootFunction

- RVA: `0x00522CC8`–`0x00522CEB` (길이 `35` bytes)
- VA: `0x0000000140522CC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `7`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiInitSystem](../../init/C5/MiInitSystem_function_00C5E6C0.md) at `0x00C5E7D9`

### Static image references
- `0x00522CC8` → RVA `0x00E0F390` (`.data`; read)
- `0x00522CD5` → RVA `0x00E0F390` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00522CC8  48 8D 05 C1 C6 8E 00            lea rax, [rip + 0x8ec6c1]
00522CCF  48 83 F8 10                     cmp rax, 0x10
00522CD3  75 0A                           jne 0x140522cdf
00522CD5  C7 05 B1 C6 8E 00 0A 00 00 00   mov dword ptr [rip + 0x8ec6b1], 0xa
00522CDF  C7 05 A7 C6 8E 00 00 00 00 00   mov dword ptr [rip + 0x8ec6a7], 0
00522CE9  C3                              ret
00522CEA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExecuteHotpatchTestBootFunction(void)
{
    if ((v_rip + 9356993) == 16) {
        *(unsigned int *)(v_rip + 9356977) = 10;
    }
    *(unsigned int *)(v_rip + 9356967) = 0;
    return v_rip + 9356993;
}
```

## 5. (Beta) C Style

```c
void ExecuteHotpatchTestBootFunction(void)
{
    if ((v_rip + 9356993) == 16) {
        *(uint32_t *)(v_rip + 0x8EC6B1) = 10;
    }
    *(uint32_t *)(v_rip + 0x8EC6A7) = 0;
    return v_rip + 9356993;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00522CC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00522CC8[BB_00522CC8]
  bb_00522CD5[BB_00522CD5]
  bb_00522CDF[BB_00522CDF]
  bb_00522CEA[BB_00522CEA]
  bb_00522CC8 -->|branch| bb_00522CDF
  bb_00522CC8 -->|fallthrough| bb_00522CD5
  bb_00522CD5 -->|flow| bb_00522CDF
```
