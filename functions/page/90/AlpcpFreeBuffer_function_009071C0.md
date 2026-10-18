# AlpcpFreeBuffer

- RVA: `0x009071C0`–`0x009071D1` (길이 `17` bytes)
- VA: `0x00000001409071C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **26**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009071C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [SmPerformStoreSwapOperation](../../text/2A/SmPerformStoreSwapOperation_function_002A8BE0.md) at `0x002A8C17`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStCleanup](../../text/3B/SMKM_STORE_SM_TRAITS_SmStCleanup_function_003B00E0.md) at `0x003B0356`
- [IoRegisterPriorityCallback](../../text/59/IoRegisterPriorityCallback_function_00597BB0.md) at `0x00597C4A`
- [IoUnregisterPriorityCallback](../../text/59/IoUnregisterPriorityCallback_function_00597D40.md) at `0x00597DDD`
- [KeDeregisterBoundCallback](../../text/5B/KeDeregisterBoundCallback_function_005B1770.md) at `0x005B17ED`
- [KeRegisterBoundCallback](../../text/5B/KeRegisterBoundCallback_function_005B1B70.md) at `0x005B1BBD`
- [ExpDeleteSiloState](../../text/65/ExpDeleteSiloState_function_00657664.md) at `0x006576CC`
- [SC_GPT::ReadEntries](../../text/6A/SC_GPT_ReadEntries_function_006A32C8.md) at `0x006A333C`
- [SC_GPT::ReadPartitionTable](../../text/6A/SC_GPT_ReadPartitionTable_function_006A34E4.md) at `0x006A3786`
- [SC_GPT::VerifyPartitionTable](../../text/6A/SC_GPT_VerifyPartitionTable_function_006A3804.md) at `0x006A3A99`
- [SC_GPT::WritePartitionTable](../../text/6A/SC_GPT_WritePartitionTable_function_006A3AD4.md) at `0x006A3F78`
- [SC_ENV_ALLOCATOR::operator delete](../../text/6A/SC_ENV_ALLOCATOR_operator_delete_function_006A3F98.md) at `0x006A3F9C`
- [ScAnsiToUnicodeString](../../text/6A/ScAnsiToUnicodeString_function_006A3FB0.md) at `0x006A402D`
- [ScAnsiToUnicodeString](../../text/6A/ScAnsiToUnicodeString_function_006A3FB0.md) at `0x006A404C`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A42E3`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A42F4`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A4305`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A4316`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A4327`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A4338`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A4349`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A435A`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A436B`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A437C`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A438D`
- [SC_DISK::~SC_DISK](../../text/6A/SC_DISK_SC_DISK_function_006A42C4.md) at `0x006A439E`
- [SC_DISK::`scalar deleting destructor&#x27;](../../text/6A/SC_DISK_scalar_deleting_destructor__function_006A43C0.md) at `0x006A43DC`
- [SC_DISK::GetStoragePropertyPost](../../text/6A/SC_DISK_GetStoragePropertyPost_function_006A4500.md) at `0x006A45C3`
- [SC_DISK::SaveStorageProperty](../../text/6A/SC_DISK_SaveStorageProperty_function_006A4B10.md) at `0x006A4B95`
- [SC_DISK::SaveStorageProperty](../../text/6A/SC_DISK_SaveStorageProperty_function_006A4B10.md) at `0x006A4BC0`
- [SC_DISK::SetPartition](../../text/6A/SC_DISK_SetPartition_function_006A4BDC.md) at `0x006A4CEC`
- [SC_MBR::ReadPartitionTable](../../text/6A/SC_MBR_ReadPartitionTable_function_006A5100.md) at `0x006A5361`
- [SC_MBR::ReadPartitionTable](../../text/6A/SC_MBR_ReadPartitionTable_function_006A5100.md) at `0x006A53A7`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A5717`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A5728`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A5739`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A574A`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A575B`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A576C`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A577A`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A5788`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A5796`
- [SC_DEVICE::~SC_DEVICE](../../text/6A/SC_DEVICE_SC_DEVICE_function_006A56F8.md) at `0x006A57A4`
- [SC_DEVICE::`scalar deleting destructor&#x27;](../../text/6A/SC_DEVICE_scalar_deleting_destructor__function_006A57C0.md) at `0x006A57DC`
- [SC_DEVICE::GetStorageProperty](../../text/6A/SC_DEVICE_GetStorageProperty_function_006A57F8.md) at `0x006A58BB`
- [SC_DEVICE::GetStorageProperty](../../text/6A/SC_DEVICE_GetStorageProperty_function_006A57F8.md) at `0x006A58EA`
- [SC_DEVICE::Initialize](../../text/6A/SC_DEVICE_Initialize_function_006A5990.md) at `0x006A59F0`
- [SC_DEVICE::SaveStorageProperty](../../text/6A/SC_DEVICE_SaveStorageProperty_function_006A5A20.md) at `0x006A5A6D`
- [SC_DEVICE::SaveStorageProperty](../../text/6A/SC_DEVICE_SaveStorageProperty_function_006A5A20.md) at `0x006A5AA8`
- [PspRundownSingleProcess](PspRundownSingleProcess_function_00906D50.md) at `0x00906E4F`
- [PspRundownSingleProcess](PspRundownSingleProcess_function_00906D50.md) at `0x00906E95`
- [PsCreateVsmEnclave](../A9/PsCreateVsmEnclave_function_00A9BCCC.md) at `0x00A9C096`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x009071C6` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009071C0  48 83 EC 28                     sub rsp, 0x28
009071C4  33 D2                           xor edx, edx
009071C6  E8 A5 B6 27 00                  call 0x140b82870
009071CB  48 83 C4 28                     add rsp, 0x28
009071CF  C3                              ret
009071D0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpFreeBuffer(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpFreeBuffer(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009071C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009071C0[BB_009071C0]
  bb_009071D0[BB_009071D0]
```
