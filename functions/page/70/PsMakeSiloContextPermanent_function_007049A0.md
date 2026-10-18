# PsMakeSiloContextPermanent

- RVA: `0x007049A0`–`0x007049C4` (길이 `36` bytes)
- VA: `0x00000001407049A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x007049B9` → [PspStorageMakeSlotReadOnly](../9E/PspStorageMakeSlotReadOnly_function_009E8350.md) (function, `0x009E8350`)

### Direct callers
- [sub_00B24EA0](../B2/Unknown_function_00B24EA0.md) at `0x00B24F2F`

### Static image references
- `0x007049A9` → RVA `0x00FCFE30` (`CACHEALI`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007049A0  48 83 EC 28                     sub rsp, 0x28
007049A4  48 85 C9                        test rcx, rcx
007049A7  75 09                           jne 0x1407049b2
007049A9  48 8B 0D 80 B4 8C 00            mov rcx, qword ptr [rip + 0x8cb480]
007049B0  EB 07                           jmp 0x1407049b9
007049B2  48 8B 89 00 06 00 00            mov rcx, qword ptr [rcx + 0x600]
007049B9  E8 92 39 2E 00                  call 0x1409e8350
007049BE  48 83 C4 28                     add rsp, 0x28
007049C2  C3                              ret
007049C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PsMakeSiloContextPermanent(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_007049B2;
    goto loc_007049B9;
loc_007049B2:
loc_007049B9:
    result = PspStorageMakeSlotReadOnly(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 9221248) + 1536), a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PsMakeSiloContextPermanent(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_007049B2;
    goto loc_007049B9;
loc_007049B2:
loc_007049B9:
    result = PspStorageMakeSlotReadOnly(*(uint64_t *)(*(uint64_t *)(v_rip + 0x8CB480) + 0x600), a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007049A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007049A0[BB_007049A0]
  bb_007049A9[BB_007049A9]
  bb_007049B2[BB_007049B2]
  bb_007049B9[BB_007049B9]
  bb_007049C3[BB_007049C3]
  bb_007049A0 -->|branch| bb_007049B2
  bb_007049A0 -->|fallthrough| bb_007049A9
  bb_007049A9 -->|branch| bb_007049B9
  bb_007049B2 -->|flow| bb_007049B9
```
