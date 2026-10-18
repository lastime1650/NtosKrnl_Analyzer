# PspDestroyProcessParameterOverrides

- RVA: `0x009F0D00`–`0x009F0D1D` (길이 `29` bytes)
- VA: `0x00000001409F0D00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x009F0D0F` → `ext-ms-win-ntos-processparameters-l1-1-0.dll!PsDestroyProcessParameterOverrides` (import, 간접 대상; import `ext-ms-win-ntos-processparameters-l1-1-0.dll!PsDestroyProcessParameterOverrides`)

### Direct callers
- [PspDeleteCreateProcessContext](../9E/PspDeleteCreateProcessContext_function_009EF4C4.md) at `0x009EF5E5`
- [PspGetProcessParameterOverrides](../A6/PspGetProcessParameterOverrides_function_00A66A50.md) at `0x00A66AB0`

### Static image references
- `0x009F0D0F` → RVA `0x00151348` (`ext-ms-win-ntos-processparameters-l1-1-0.dll!PsDestroyProcessParameterOverrides (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F0D00  48 83 EC 28                     sub rsp, 0x28
009F0D04  48 85 C9                        test rcx, rcx
009F0D07  75 06                           jne 0x1409f0d0f
009F0D09  48 83 C4 28                     add rsp, 0x28
009F0D0D  C3                              ret
009F0D0E  CC                              int3
009F0D0F  48 FF 15 32 06 76 FF            call qword ptr [rip - 0x89f9ce]
009F0D16  0F 1F 44 00 00                  nop dword ptr [rax + rax]
009F0D1B  EB EC                           jmp 0x1409f0d09
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspDestroyProcessParameterOverrides(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_009F0D0F;
loc_009F0D09:
    v_rsp = (v_rsp) + (40);
    return result;
loc_009F0D0F:
    result = ext_ms_win_ntos_processparameters_l1_1_0_dll_PsDestroyProcessParameterOverrides(a1, a2, a3, a4);
    goto loc_009F0D09;
}
```

## 5. (Beta) C Style

```c
int64_t PspDestroyProcessParameterOverrides(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_009F0D0F;
loc_009F0D09:
    local_rsp = (local_rsp) + (40);
    return result;
loc_009F0D0F:
    result = kernel_indirect_call(Arg1, a2, a3, a4);
    goto loc_009F0D09;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F0D00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009F0D00[BB_009F0D00]
  bb_009F0D09[BB_009F0D09]
  bb_009F0D0E[BB_009F0D0E]
  bb_009F0D0F[BB_009F0D0F]
  bb_009F0D00 -->|branch| bb_009F0D0F
  bb_009F0D00 -->|fallthrough| bb_009F0D09
  bb_009F0D0E -->|flow| bb_009F0D0F
  bb_009F0D0F -->|branch| bb_009F0D09
```
