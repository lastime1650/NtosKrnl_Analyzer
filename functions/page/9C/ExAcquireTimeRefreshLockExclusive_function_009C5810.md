# ExAcquireTimeRefreshLockExclusive

- RVA: `0x009C5810`–`0x009C586D` (길이 `93` bytes)
- VA: `0x00000001409C5810`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `93/93` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x009C5833` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009C5858` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [ExCleanTimerResolutionRequest](../../text/4B/ExCleanTimerResolutionRequest_function_004B0C58.md) at `0x004B0C83`
- [ExpReadLeapSecondData](../7C/ExpReadLeapSecondData_function_007C5EAC.md) at `0x007C60C5`
- [ExpRefreshSystemTime](../7C/ExpRefreshSystemTime_function_007C6264.md) at `0x007C6295`
- [ExpTimeZoneInitSiloState](../7C/ExpTimeZoneInitSiloState_function_007C6430.md) at `0x007C64B1`
- [NtSetSystemTime](../7C/NtSetSystemTime_function_007C65F0.md) at `0x007C671B`
- [NtSetSystemTime](../7C/NtSetSystemTime_function_007C65F0.md) at `0x007C679A`
- [NtSetSystemTime](../7C/NtSetSystemTime_function_007C65F0.md) at `0x007C688C`
- [NtSetTimerResolution](NtSetTimerResolution_function_009C5170.md) at `0x009C53E5`
- [ExUpdateTimerResolutionPolicy](ExUpdateTimerResolutionPolicy_function_009C579C.md) at `0x009C57D8`
- [NtSetSystemInformation](../AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF4D8C`
- [ExpTimeRefreshWork](../../pagelk/B7/ExpTimeRefreshWork_function_00B72A80.md) at `0x00B72A84`
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7F633`
- [sub_00B80364](../../pagelk/B8/Unknown_function_00B80364.md) at `0x00B80389`
- [Phase1InitializationDiscard](../../init/C1/Phase1InitializationDiscard_function_00C1C728.md) at `0x00C1D6AB`

### Static image references
- `0x009C581F` → RVA `0x00EFEFC8` (`.data`; read)
- `0x009C5838` → RVA `0x00EFEFC8` (`.data`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009C5833` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009C5858` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009C5810  40 53                           push rbx
009C5812  48 83 EC 20                     sub rsp, 0x20
009C5816  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009C581F  48 8D 0D A2 97 53 00            lea rcx, [rip + 0x5397a2]
009C5826  45 33 C0                        xor r8d, r8d
009C5829  33 D2                           xor edx, edx
009C582B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
009C5832  90                              nop
009C5833  E8 F8 A9 84 FF                  call 0x140210230
009C5838  F0 48 0F BA 2D 86 97 53 00 00   lock bts qword ptr [rip + 0x539786], 0
009C5842  48 8B D8                        mov rbx, rax
009C5845  73 16                           jae 0x1409c585d
009C5847  4C 8D 05 7A 97 53 00            lea r8, [rip + 0x53977a]
009C584E  48 8B D0                        mov rdx, rax
009C5851  48 8D 0D 70 97 53 00            lea rcx, [rip + 0x539770]
009C5858  E8 33 A4 84 FF                  call 0x14020fc90
009C585D  48 85 DB                        test rbx, rbx
009C5860  74 04                           je 0x1409c5866
009C5862  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
009C5866  48 83 C4 20                     add rsp, 0x20
009C586A  5B                              pop rbx
009C586B  C3                              ret
009C586C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExAcquireTimeRefreshLockExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 5478306, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 5478266;
        a2 = result;
        a1 = v_rip + 5478256;
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
int64_t ExAcquireTimeRefreshLockExclusive(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 5478306, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 5478266;
        Arg2 = result;
        Arg1 = v_rip + 5478256;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009C5810&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009C5810[BB_009C5810]
  bb_009C5847[BB_009C5847]
  bb_009C585D[BB_009C585D]
  bb_009C5862[BB_009C5862]
  bb_009C5866[BB_009C5866]
  bb_009C586C[BB_009C586C]
  bb_009C5810 -->|branch| bb_009C585D
  bb_009C5810 -->|fallthrough| bb_009C5847
  bb_009C5847 -->|flow| bb_009C585D
  bb_009C585D -->|branch| bb_009C5866
  bb_009C585D -->|fallthrough| bb_009C5862
  bb_009C5862 -->|flow| bb_009C5866
```
