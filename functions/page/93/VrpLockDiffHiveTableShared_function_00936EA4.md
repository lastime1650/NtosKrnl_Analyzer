# VrpLockDiffHiveTableShared

- RVA: `0x00936EA4`–`0x00936F09` (길이 `101` bytes)
- VA: `0x0000000140936EA4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `26`개 명령, `101/101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00936EC7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00936EF4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [VrpFindOrCreateDiffHiveEntryForMountPoint](VrpFindOrCreateDiffHiveEntryForMountPoint_function_00936290.md) at `0x009362AF`
- [VrpFindDiffHiveEntryForMountPoint](VrpFindDiffHiveEntryForMountPoint_function_00936DF0.md) at `0x00936DF9`

### Static image references
- `0x00936EB3` → RVA `0x00EF02B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00936EC7` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00936EF4` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00936EA4  40 53                           push rbx
00936EA6  48 83 EC 20                     sub rsp, 0x20
00936EAA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00936EB3  48 8D 0D F6 93 5B 00            lea rcx, [rip + 0x5b93f6]
00936EBA  45 33 C0                        xor r8d, r8d
00936EBD  33 D2                           xor edx, edx
00936EBF  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00936EC6  90                              nop
00936EC7  E8 64 93 8D FF                  call 0x140210230
00936ECC  48 8B D8                        mov rbx, rax
00936ECF  BA 11 00 00 00                  mov edx, 0x11
00936ED4  33 C0                           xor eax, eax
00936ED6  F0 48 0F B1 15 D1 93 5B 00      lock cmpxchg qword ptr [rip + 0x5b93d1], rdx
00936EDF  74 18                           je 0x140936ef9
00936EE1  4C 8D 0D C8 93 5B 00            lea r9, [rip + 0x5b93c8]
00936EE8  4C 8B C3                        mov r8, rbx
00936EEB  33 D2                           xor edx, edx
00936EED  48 8D 0D BC 93 5B 00            lea rcx, [rip + 0x5b93bc]
00936EF4  E8 53 95 8D FF                  call 0x14021044c
00936EF9  48 85 DB                        test rbx, rbx
00936EFC  74 04                           je 0x140936f02
00936EFE  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
00936F02  48 83 C4 20                     add rsp, 0x20
00936F06  5B                              pop rbx
00936F07  C3                              ret
00936F08  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpLockDiffHiveTableShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6001654, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6001608;
        a3 = 0;
        a2 = 0;
        a1 = v_rip + 6001596;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
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
int64_t VrpLockDiffHiveTableShared(int64_t Arg1, int32_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6001654, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rip + 6001608;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_rip + 6001596;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00936EA4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00936EA4[BB_00936EA4]
  bb_00936EE1[BB_00936EE1]
  bb_00936EF9[BB_00936EF9]
  bb_00936EFE[BB_00936EFE]
  bb_00936F02[BB_00936F02]
  bb_00936F08[BB_00936F08]
  bb_00936EA4 -->|branch| bb_00936EF9
  bb_00936EA4 -->|fallthrough| bb_00936EE1
  bb_00936EE1 -->|flow| bb_00936EF9
  bb_00936EF9 -->|branch| bb_00936F02
  bb_00936EF9 -->|fallthrough| bb_00936EFE
  bb_00936EFE -->|flow| bb_00936F02
```
