# RtlCheckTokenMembership

- RVA: `0x003A5A10`–`0x003A5A25` (길이 `21` bytes)
- VA: `0x00000001403A5A10`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003A5A1A` → [RtlCheckTokenMembershipEx](RtlCheckTokenMembershipEx_function_003A5A30.md) (function, `0x003A5A30`)

### Direct callers
- [NtFilterBootOption](../../page/7A/NtFilterBootOption_function_007A1BE0.md) at `0x007A1CA0`
- [EtwpUserInAdminOrLogUsersGroup](../../page/7B/EtwpUserInAdminOrLogUsersGroup_function_007B7D50.md) at `0x007B7D7A`
- [EtwpUserInAdminOrLogUsersGroup](../../page/7B/EtwpUserInAdminOrLogUsersGroup_function_007B7D50.md) at `0x007B7DBA`
- [PopValidateContextMembership](../../page/91/PopValidateContextMembership_function_009129AC.md) at `0x009129BF`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A204EB`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A20546`
- [RtlCapabilityCheck](../../page/A2/RtlCapabilityCheck_function_00A20340.md) at `0x00A20697`
- [ExpCheckIRTimerAccess](../../page/A2/ExpCheckIRTimerAccess_function_00A2C83C.md) at `0x00A2C88E`
- [PopIsRunningAsLocalSystem](../../page/A8/PopIsRunningAsLocalSystem_function_00A88594.md) at `0x00A885AB`
- [PopPowerInformationInternal](../../page/A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8C617`
- [PopNetUpdateStandbyRequest](../../page/AD/PopNetUpdateStandbyRequest_function_00ADB704.md) at `0x00ADB730`
- [NtSetSystemInformation](../../page/AF/NtSetSystemInformation_function_00AF4A60.md) at `0x00AF670A`
- [sub_00B37578](../../page/B3/Unknown_function_00B37578.md) at `0x00B375B1`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003A5A10  48 83 EC 28                     sub rsp, 0x28
003A5A14  4D 8B C8                        mov r9, r8
003A5A17  45 33 C0                        xor r8d, r8d
003A5A1A  E8 11 00 00 00                  call 0x1403a5a30
003A5A1F  48 83 C4 28                     add rsp, 0x28
003A5A23  C3                              ret
003A5A24  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlCheckTokenMembership(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = 0;
    result = RtlCheckTokenMembershipEx(a1, a2, a3, a3);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlCheckTokenMembership(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = 0;
    result = RtlCheckTokenMembershipEx(Arg1, Arg2, Arg3, Arg3);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003A5A10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003A5A10[BB_003A5A10]
  bb_003A5A24[BB_003A5A24]
```
