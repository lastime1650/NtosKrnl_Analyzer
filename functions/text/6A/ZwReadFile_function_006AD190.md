# ZwReadFile

- RVA: `0x006AD190`–`0x006AD1AF` (길이 `31` bytes)
- VA: `0x00000001406AD190`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFED8`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **16**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [CmpDoFileRead](../48/CmpDoFileRead_function_00485658.md) at `0x00485723`
- [SecureDump_LoadCertAndProvisionKey](../5A/SecureDump_LoadCertAndProvisionKey_function_005A2E04.md) at `0x005A2FC6`
- [RtlInitializeBootStatDataCache](../5E/RtlInitializeBootStatDataCache_function_005E78F0.md) at `0x005E7952`
- [RtlInitializeBootStatDataCache](../5E/RtlInitializeBootStatDataCache_function_005E78F0.md) at `0x005E79DF`
- [SepAppIdentityFromImageHash](../60/SepAppIdentityFromImageHash_function_00607AA4.md) at `0x00607C83`
- [DifZwReadFileWrapper](../64/DifZwReadFileWrapper_function_00648DA0.md) at `0x00648EE6`
- [PopLoadFileInMemory](../../page/75/PopLoadFileInMemory_function_007540E4.md) at `0x007541F6`
- [SshpSessionManagerOpenControlTrace](../../page/77/SshpSessionManagerOpenControlTrace_function_007744C0.md) at `0x00774557`
- [RtlCheckBootStatusIntegrity](../../page/79/RtlCheckBootStatusIntegrity_function_00790464.md) at `0x007904C7`
- [RtlCheckBootStatusIntegrity](../../page/79/RtlCheckBootStatusIntegrity_function_00790464.md) at `0x0079055F`
- [RtlInitializeBootStatusDataBlackBox](../../page/79/RtlInitializeBootStatusDataBlackBox_function_00790694.md) at `0x0079070D`
- [CMFSystemThreadRoutine](../../page/7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3CB6`
- [CMFSystemThreadRoutine](../../page/7D/CMFSystemThreadRoutine_function_007D3A70.md) at `0x007D3F2B`
- [EtwpRealtimeRestoreBuffer](../../page/9B/EtwpRealtimeRestoreBuffer_function_009BF360.md) at `0x009BF3CD`
- [EtwpRealtimeRestoreBuffer](../../page/9B/EtwpRealtimeRestoreBuffer_function_009BF360.md) at `0x009BF464`
- [EtwpUpdateFileHeader](../../page/9C/EtwpUpdateFileHeader_function_009C082C.md) at `0x009C0A00`
- [EtwpFinalizeHeader](../../page/9C/EtwpFinalizeHeader_function_009C1EF0.md) at `0x009C1FF9`
- [EtwpFinalizeHeader](../../page/9C/EtwpFinalizeHeader_function_009C1EF0.md) at `0x009C2278`
- [RtlpGetSetBootStatusData](../../page/A4/RtlpGetSetBootStatusData_function_00A4CD64.md) at `0x00A4CDD4`
- [RtlpGetSetBootStatusData](../../page/A4/RtlpGetSetBootStatusData_function_00A4CD64.md) at `0x00A4CF90`
- [EtwpRealtimeRestoreState](../../page/AC/EtwpRealtimeRestoreState_function_00AC6A74.md) at `0x00AC6B38`
- [EmInitSystem](../../init/C7/EmInitSystem_function_00C71150.md) at `0x00C715EE`

### Static image references
- `0x006AD19C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD1A9` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD190  48 8B C4                        mov rax, rsp
006AD193  FA                              cli
006AD194  48 83 EC 10                     sub rsp, 0x10
006AD198  50                              push rax
006AD199  9C                              pushfq
006AD19A  6A 10                           push 0x10
006AD19C  48 8D 05 BD 62 00 00            lea rax, [rip + 0x62bd]
006AD1A3  50                              push rax
006AD1A4  B8 06 00 00 00                  mov eax, 6
006AD1A9  E9 12 78 01 00                  jmp 0x1406c49c0
006AD1AE  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwReadFile(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwReadFile(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD190&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD190[BB_006AD190]
  bb_006AD1AE[BB_006AD1AE]
```
