# sub_00B218E0

- RVA: `0x00B218E0`–`0x00B21983` (길이 `163` bytes)
- VA: `0x0000000140B218E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008A6F4`
- 디코드: `37`개 명령, `163/163` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **6**

### Outgoing calls
- `0x00B218FD` → [PopPrintUserActivityPresence](../91/PopPrintUserActivityPresence_function_00915614.md) (function, `0x00915614`)
- `0x00B21911` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (function, `0x0048EF24`)
- `0x00B21919` → [PopDiagTraceSessionStateCounted](../AA/PopDiagTraceSessionStateCounted_function_00AA2C2C.md) (function, `0x00AA2C2C`)
- `0x00B2192F` → [PopSetPowerSettingValueAcDc](../91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (function, `0x00914D6C`)
- `0x00B21946` → [PopUmpoSendUserPresencePredictionAction](../AD/PopUmpoSendUserPresencePredictionAction_function_00ADA83C.md) (function, `0x00ADA83C`)
- `0x00B21978` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B218E0` → RVA `0x00E67A4C` (`.data`; read)
- `0x00B218F0` → RVA `0x00E67A4C` (`.data`; write)
- `0x00B218F7` → RVA `0x00E0C398` (`.data`; write)
- `0x00B21905` → RVA `0x00B031A0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00B21928` → RVA `0x0001ED50` (`.rdata`; read)
- `0x00B2195A` → RVA `0x00020B90` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B21911` → [PopPrintEx](../../text/48/PopPrintEx_function_0048EF24.md) (`PAGE` → `.text`)
  - `0x00B21978` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B2197E` → [PopEvaluateGlobalUserStatus + 0x3B](../91/PopEvaluateGlobalUserStatus_function_009155C8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B218E0  44 8B 0D 65 61 34 00            mov r9d, dword ptr [rip + 0x346165]
00B218E7  8B CB                           mov ecx, ebx
00B218E9  41 FF C1                        inc r9d
00B218EC  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
00B218F0  44 89 0D 55 61 34 00            mov dword ptr [rip + 0x346155], r9d
00B218F7  89 1D 9B AA 2E 00               mov dword ptr [rip + 0x2eaa9b], ebx
00B218FD  E8 12 3D DF FF                  call 0x140915614
00B21902  4C 8B C0                        mov r8, rax
00B21905  48 8D 15 94 18 FE FF            lea rdx, [rip - 0x1e76c]
00B2190C  B9 03 00 00 00                  mov ecx, 3
00B21911  E8 0E D6 96 FF                  call 0x14048ef24
00B21916  44 8B C3                        mov r8d, ebx
00B21919  E8 0E 13 F8 FF                  call 0x140aa2c2c
00B2191E  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
00B21923  BA 04 00 00 00                  mov edx, 4
00B21928  48 8D 0D 21 D4 4F FF            lea rcx, [rip - 0xb02bdf]
00B2192F  E8 38 34 DF FF                  call 0x140914d6c
00B21934  33 C0                           xor eax, eax
00B21936  85 DB                           test ebx, ebx
00B21938  0F 95 C0                        setne al
00B2193B  33 C9                           xor ecx, ecx
00B2193D  85 DB                           test ebx, ebx
00B2193F  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00B21943  0F 95 C1                        setne cl
00B21946  E8 F1 8E FB FF                  call 0x140ada83c
00B2194B  83 64 24 30 00                  and dword ptr [rsp + 0x30], 0
00B21950  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00B21955  83 64 24 28 00                  and dword ptr [rsp + 0x28], 0
00B2195A  48 8D 0D 2F F2 4F FF            lea rcx, [rip - 0xb00dd1]
00B21961  8B 05 E5 60 34 00               mov eax, dword ptr [rip + 0x3460e5]
00B21967  45 33 C9                        xor r9d, r9d
00B2196A  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B21970  89 44 24 5C                     mov dword ptr [rsp + 0x5c], eax
00B21974  45 8D 41 08                     lea r8d, [r9 + 8]
00B21978  E8 93 F3 B8 FF                  call 0x1406b0d10
00B2197D  90                              nop
00B2197E  E9 80 3C DF FF                  jmp 0x140915603
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B218E0(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    unsigned __int64 v_stack_p20;
    unsigned int v_stack_p50;
    unsigned int v_stack_p58;
    unsigned int v_stack_p5C;

    a4 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3432805))) + 1);
    v_stack_p50 = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 3432789) = (unsigned int)(a4);
    *(unsigned int *)(v_rip + 3058331) = (unsigned int)(v_rbx);
    result = PopPrintUserActivityPresence((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    result = PopPrintEx(3, v_rip - 124780, result, a4);
    result = PopDiagTraceSessionStateCounted(3, v_rip - 124780, (unsigned int)((unsigned int)(v_rbx)), a4);
    result = PopSetPowerSettingValueAcDc(v_rip - 11545567, 4, a10, a4);
    result = 0;
    result = ((unsigned int)(v_rbx) != 0) ? 1 : 0;
    a1 = 0;
    v_stack_p58 = (unsigned int)(result);
    a1 = ((unsigned int)(v_rbx) != 0) ? 1 : 0;
    result = PopUmpoSendUserPresencePredictionAction(a1, 4, a10, a4);
    a4 = 0;
    v_stack_p5C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3432677)));
    result = ZwUpdateWnfStateData(v_rip - 11537873, a11, a4 + 8, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B218E0(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    int64_t result;
    uint64_t v_stack_p20;
    uint32_t v_stack_p50;
    uint32_t v_stack_p58;
    uint32_t v_stack_p5C;

    Arg4 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x346165))) + 1);
    v_stack_p50 = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x346155) = (uint32_t)(Arg4);
    *(uint32_t *)(v_rip + 0x2EAA9B) = (uint32_t)(local_rbx);
    result = PopPrintUserActivityPresence((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, Arg4);
    result = PopPrintEx(3, v_rip - 124780, result, Arg4);
    result = PopDiagTraceSessionStateCounted(3, v_rip - 124780, (uint32_t)((uint32_t)(local_rbx)), Arg4);
    result = PopSetPowerSettingValueAcDc(v_rip - 11545567, 4, Arg10, Arg4);
    result = 0;
    result = ((uint32_t)(local_rbx) != 0) ? 1 : 0;
    Arg1 = 0;
    v_stack_p58 = (uint32_t)(result);
    Arg1 = ((uint32_t)(local_rbx) != 0) ? 1 : 0;
    result = PopUmpoSendUserPresencePredictionAction(Arg1, 4, Arg10, Arg4);
    Arg4 = 0;
    v_stack_p5C = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3460E5)));
    result = ZwUpdateWnfStateData(v_rip - 11537873, Arg11, Arg4 + 8, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B218E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B218E0[BB_00B218E0]
```
