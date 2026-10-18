# HalpMiscInitializeTelemetry

- RVA: `0x00707DFC`–`0x00707E3C` (길이 `64` bytes)
- VA: `0x0000000140707DFC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `17`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00707E13` → [EtwRegister](../92/EtwRegister_function_00920960.md) (function, `0x00920960`)
- `0x00707E2F` → [TraceLoggingRegisterEx_EtwRegister_EtwSetInformation](../92/TraceLoggingRegisterEx_EtwRegister_EtwSetInformation_function_009208A0.md) (function, `0x009208A0`)

### Direct callers
- [HalpMiscInitSystem](../../pagelk/B5/HalpMiscInitSystem_function_00B5D510.md) at `0x00B5D527`

### Static image references
- `0x00707E00` → RVA `0x00FC22B8` (`.data`; read)
- `0x00707E0C` → RVA `0x00022898` (`.rdata`; read)
- `0x00707E1C` → RVA `0x00FC22C0` (`.data`; write)
- `0x00707E26` → RVA `0x00E03B28` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00707DFC  48 83 EC 28                     sub rsp, 0x28
00707E00  4C 8D 0D B1 A4 8B 00            lea r9, [rip + 0x8ba4b1]
00707E07  45 33 C0                        xor r8d, r8d
00707E0A  33 D2                           xor edx, edx
00707E0C  48 8D 0D 85 AA 91 FF            lea rcx, [rip - 0x6e557b]
00707E13  E8 48 8B 21 00                  call 0x140920960
00707E18  85 C0                           test eax, eax
00707E1A  78 07                           js 0x140707e23
00707E1C  C6 05 9D A4 8B 00 01            mov byte ptr [rip + 0x8ba49d], 1
00707E23  45 33 C0                        xor r8d, r8d
00707E26  48 8D 0D FB BC 6F 00            lea rcx, [rip + 0x6fbcfb]
00707E2D  33 D2                           xor edx, edx
00707E2F  E8 6C 8A 21 00                  call 0x1409208a0
00707E34  33 C0                           xor eax, eax
00707E36  48 83 C4 28                     add rsp, 0x28
00707E3A  C3                              ret
00707E3B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMiscInitializeTelemetry(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = 0;
    a2 = 0;
    result = EtwRegister(v_rip - 7230843, a2, a3, v_rip + 9151665);
    if (!(sign_flag)) {
        *(unsigned __int8 *)(v_rip + 9151645) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 7322875, a2, a3, v_rip + 9151665);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpMiscInitializeTelemetry(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = 0;
    Arg2 = 0;
    result = EtwRegister(v_rip - 7230843, Arg2, Arg3, v_rip + 9151665);
    if (!(sign_flag)) {
        *(uint8_t *)(v_rip + 0x8BA49D) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = TraceLoggingRegisterEx_EtwRegister_EtwSetInformation(v_rip + 7322875, Arg2, Arg3, v_rip + 9151665);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00707DFC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00707DFC[BB_00707DFC]
  bb_00707E1C[BB_00707E1C]
  bb_00707E23[BB_00707E23]
  bb_00707E3B[BB_00707E3B]
  bb_00707DFC -->|branch| bb_00707E23
  bb_00707DFC -->|fallthrough| bb_00707E1C
  bb_00707E1C -->|flow| bb_00707E23
```
