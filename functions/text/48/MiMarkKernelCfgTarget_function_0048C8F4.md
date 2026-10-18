# MiMarkKernelCfgTarget

- RVA: `0x0048C8F4`–`0x0048C914` (길이 `32` bytes)
- VA: `0x000000014048C8F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0048C90D` → [VslEnableKernelCfgTarget](../../page/A4/VslEnableKernelCfgTarget_function_00A4585C.md) (function, `0x00A4585C`)

### Direct callers
- [MmGetSystemRoutineAddress](../../page/90/MmGetSystemRoutineAddress_function_0090EFE0.md) at `0x0090F05F`
- [MiMarkKernelCfgAddressTakenImports](../../page/AA/MiMarkKernelCfgAddressTakenImports_function_00AA262C.md) at `0x00AA2696`

### Static image references
- `0x0048C8F8` → RVA `0x00FC6A88` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0048C90D` → [VslEnableKernelCfgTarget](../../page/A4/VslEnableKernelCfgTarget_function_00A4585C.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0048C8F4  48 83 EC 28                     sub rsp, 0x28
0048C8F8  48 F7 05 85 A1 B3 00 00 00 04 00  test qword ptr [rip + 0xb3a185], 0x40000
0048C903  75 08                           jne 0x14048c90d
0048C905  33 C0                           xor eax, eax
0048C907  48 83 C4 28                     add rsp, 0x28
0048C90B  C3                              ret
0048C90C  CC                              int3
0048C90D  E8 4A 8F 5B 00                  call 0x140a4585c
0048C912  EB F1                           jmp 0x14048c905
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMarkKernelCfgTarget(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((*(unsigned __int64 *)(v_rip + 11772293)) & (0x40000ULL)) != 0) goto loc_0048C90D;
loc_0048C905:
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
loc_0048C90D:
    result = VslEnableKernelCfgTarget(a1, a2, a3, a4);
    goto loc_0048C905;
}
```

## 5. (Beta) C Style

```c
void MiMarkKernelCfgTarget(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((*(uint64_t *)(v_rip + 0xB3A185)) & (0x40000ULL)) != 0) goto loc_0048C90D;
loc_0048C905:
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
loc_0048C90D:
    result = VslEnableKernelCfgTarget(a1, a2, a3, a4);
    goto loc_0048C905;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0048C8F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0048C8F4[BB_0048C8F4]
  bb_0048C905[BB_0048C905]
  bb_0048C90C[BB_0048C90C]
  bb_0048C90D[BB_0048C90D]
  bb_0048C8F4 -->|branch| bb_0048C90D
  bb_0048C8F4 -->|fallthrough| bb_0048C905
  bb_0048C90C -->|flow| bb_0048C90D
  bb_0048C90D -->|branch| bb_0048C905
```
