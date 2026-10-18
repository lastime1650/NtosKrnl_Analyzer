# RtlInitKernelModeSpecialMachineFrameEntries

- RVA: `0x00C4763C`–`0x00C47657` (길이 `27` bytes)
- VA: `0x0000000140C4763C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C4764C` → [RtlpInitMachineFrameEntries](RtlpInitMachineFrameEntries_function_00C476D4.md) (function, `0x00C476D4`)

### Direct callers
- [KiInitializeKernel](../../pagelk/B6/KiInitializeKernel_function_00B68D20.md) at `0x00B69142`

### Static image references
- `0x00C47645` → RVA `0x00E01EC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C4763C  48 83 EC 28                     sub rsp, 0x28
00C47640  BA 03 00 00 00                  mov edx, 3
00C47645  48 8D 0D 7C A8 1B 00            lea rcx, [rip + 0x1ba87c]
00C4764C  E8 83 00 00 00                  call 0x140c476d4
00C47651  48 83 C4 28                     add rsp, 0x28
00C47655  C3                              ret
00C47656  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlInitKernelModeSpecialMachineFrameEntries(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlpInitMachineFrameEntries(v_rip + 1812604, 3, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void RtlInitKernelModeSpecialMachineFrameEntries(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlpInitMachineFrameEntries(v_rip + 1812604, 3, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C4763C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C4763C[BB_00C4763C]
  bb_00C47656[BB_00C47656]
```
