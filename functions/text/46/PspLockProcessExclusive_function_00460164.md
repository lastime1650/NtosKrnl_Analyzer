# PspLockProcessExclusive

- RVA: `0x00460164`–`0x004601B8` (길이 `84` bytes)
- VA: `0x0000000140460164`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `84/84` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **20**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00460185` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0046019E` → [ExfAcquirePushLockExclusiveEx](../20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PsThawMultiProcess](../45/PsThawMultiProcess_function_0045FFE0.md) at `0x00460019`
- [PspSyscallProviderOptIn](../../page/77/PspSyscallProviderOptIn_function_0077E79C.md) at `0x0077E893`
- [PsTerminateMinimalProcess](../../page/78/PsTerminateMinimalProcess_function_007861A8.md) at `0x007861F1`
- [PspCreatePicoProcess](../../page/78/PspCreatePicoProcess_function_007873B0.md) at `0x00787567`
- [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) at `0x008A2E45`
- [DbgkForwardException](../../page/8A/DbgkForwardException_function_008A2D60.md) at `0x008A305D`
- [PsSetProcessTelemetryAppState](../../page/8A/PsSetProcessTelemetryAppState_function_008A35F0.md) at `0x008A365E`
- [PspExitLastThread](../../page/90/PspExitLastThread_function_00904184.md) at `0x009043EC`
- [PspExitLastThread](../../page/90/PspExitLastThread_function_00904184.md) at `0x00904400`
- [PspRundownSingleProcess](../../page/90/PspRundownSingleProcess_function_00906D50.md) at `0x00907049`
- [PspAllocateAndQueryProcessNotificationChannel](../../page/9D/PspAllocateAndQueryProcessNotificationChannel_function_009D0140.md) at `0x009D0247`
- [sub_009F6528](../../page/9F/Unknown_function_009F6528.md) at `0x009F6546`
- [PspAllocateProcess](../../page/A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A1622B`
- [PspSetProcessForegroundBackgroundRequest](../../page/A4/PspSetProcessForegroundBackgroundRequest_function_00A45DCC.md) at `0x00A45E99`
- [PsSetProcessWin32Process](../../page/A5/PsSetProcessWin32Process_function_00A5F4F0.md) at `0x00A5F520`
- [PsSetProcessFaultInformation](../../page/A7/PsSetProcessFaultInformation_function_00A75400.md) at `0x00A7544E`
- [PsSetProcessFaultInformation](../../page/A7/PsSetProcessFaultInformation_function_00A75400.md) at `0x00A75505`
- [PspThreadDelete](../../page/A7/PspThreadDelete_function_00A79C20.md) at `0x00A79D5C`
- [PsFreezeProcess](../../page/AA/PsFreezeProcess_function_00AA6D04.md) at `0x00AA6D79`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6324`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6A79`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6C22`
- [NtSetInformationProcess](../../page/AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE7522`
- [NtTerminateProcess](../../page/AE/NtTerminateProcess_function_00AEC320.md) at `0x00AEC4AF`
- [sub_00B19CFC](../../page/B1/Unknown_function_00B19CFC.md) at `0x00B19D17`
- [sub_00B4102A](../../page/B4/Unknown_function_00B4102A.md) at `0x00B41045`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00460164  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00460169  57                              push rdi
0046016A  48 83 EC 20                     sub rsp, 0x20
0046016E  66 FF 8A E4 01 00 00            dec word ptr [rdx + 0x1e4]
00460175  48 8D B9 C8 01 00 00            lea rdi, [rcx + 0x1c8]
0046017C  48 8B CF                        mov rcx, rdi
0046017F  45 33 C0                        xor r8d, r8d
00460182  33 D2                           xor edx, edx
00460184  90                              nop
00460185  E8 A6 00 DB FF                  call 0x140210230
0046018A  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00460190  48 8B D8                        mov rbx, rax
00460193  73 0E                           jae 0x1404601a3
00460195  4C 8B C7                        mov r8, rdi
00460198  48 8B D0                        mov rdx, rax
0046019B  48 8B CF                        mov rcx, rdi
0046019E  E8 ED FA DA FF                  call 0x14020fc90
004601A3  48 85 DB                        test rbx, rbx
004601A6  74 04                           je 0x1404601ac
004601A8  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
004601AC  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004601B1  48 83 C4 20                     add rsp, 0x20
004601B5  5F                              pop rdi
004601B6  C3                              ret
004601B7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspLockProcessExclusive(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 456, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 456;
        a2 = result;
        a1 = a1 + 456;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspLockProcessExclusive(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 456, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 456;
        Arg2 = result;
        Arg1 = Arg1 + 456;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x1C8` | `64` | `R` |
| `Arg2` | `+ 0x1E4` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00460164&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00460164[BB_00460164]
  bb_00460195[BB_00460195]
  bb_004601A3[BB_004601A3]
  bb_004601A8[BB_004601A8]
  bb_004601AC[BB_004601AC]
  bb_004601B7[BB_004601B7]
  bb_00460164 -->|branch| bb_004601A3
  bb_00460164 -->|fallthrough| bb_00460195
  bb_00460195 -->|flow| bb_004601A3
  bb_004601A3 -->|branch| bb_004601AC
  bb_004601A3 -->|fallthrough| bb_004601A8
  bb_004601A8 -->|flow| bb_004601AC
```
