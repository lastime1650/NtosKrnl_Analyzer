# ZwQueryVirtualMemory

- RVA: `0x006AD530`–`0x006AD54F` (길이 `31` bytes)
- VA: `0x00000001406AD530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C0034`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **18**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_0034C8E9](../34/Unknown_function_0034C8E9.md) at `0x0034C998`
- [SMKM_STORE&lt;SM_TRAITS&gt;::SmStPrioritizeRegionsStore](../34/SMKM_STORE_SM_TRAITS_SmStPrioritizeRegionsStore_function_0034DE28.md) at `0x0034DFE9`
- [KiVerifyContextXStateCetUEnabled](../3D/KiVerifyContextXStateCetUEnabled_function_003D75C0.md) at `0x003D760C`
- [sub_0041E9E0](../41/Unknown_function_0041E9E0.md) at `0x0041EA20`
- [RtlpCreateHeap](../4E/RtlpCreateHeap_function_004E1904.md) at `0x004E1E5C`
- [RtlpCreateHeap](../4E/RtlpCreateHeap_function_004E1904.md) at `0x004E1EDE`
- [RtlpHpFixedHeapCreate](../60/RtlpHpFixedHeapCreate_function_006038A0.md) at `0x00603939`
- [RtlpHpFixedHeapCreate](../60/RtlpHpFixedHeapCreate_function_006038A0.md) at `0x0060395F`
- [EtwTimLogControlProtectionUserModeReturnMismatch](../../page/7B/EtwTimLogControlProtectionUserModeReturnMismatch_function_007BA9D4.md) at `0x007BABFB`
- [EtwTimLogControlProtectionUserModeReturnMismatch](../../page/7B/EtwTimLogControlProtectionUserModeReturnMismatch_function_007BA9D4.md) at `0x007BACE4`
- [EtwTimLogUserCetSetContextIpValidationFailure](../../page/7B/EtwTimLogUserCetSetContextIpValidationFailure_function_007BB920.md) at `0x007BBA93`
- [PspFreeUserFiberShadowStack](../../page/87/PspFreeUserFiberShadowStack_function_0087F9A0.md) at `0x0087FA4E`
- [PspFreeCurrentThreadUserShadowStack](../../page/87/PspFreeCurrentThreadUserShadowStack_function_0087FD7C.md) at `0x0087FDBE`
- [EtwTiLogProtectExecVm](../../page/88/EtwTiLogProtectExecVm_function_00881A48.md) at `0x00881BA3`
- [EtwTiLogProtectExecVm](../../page/88/EtwTiLogProtectExecVm_function_00881A48.md) at `0x00881BF2`
- [PspGetScpCfgFunctions](../../page/8C/PspGetScpCfgFunctions_function_008CE498.md) at `0x008CE4E9`
- [LdrpResGetMappingSize](../../page/99/LdrpResGetMappingSize_function_00991614.md) at `0x00991761`
- [sub_009A13B8](../../page/9A/Unknown_function_009A13B8.md) at `0x009A141C`
- [sub_009A13B8](../../page/9A/Unknown_function_009A13B8.md) at `0x009A146C`
- [EtwTiLogReadWriteVm](../../page/9B/EtwTiLogReadWriteVm_function_009BB7C8.md) at `0x009BB907`
- [EtwTiLogReadWriteVm](../../page/9B/EtwTiLogReadWriteVm_function_009BB7C8.md) at `0x009BB955`
- [EtwpTiQueryVad](../../page/A0/EtwpTiQueryVad_function_00A03A70.md) at `0x00A03AF8`
- [EtwpTiQueryVad](../../page/A0/EtwpTiQueryVad_function_00A03A70.md) at `0x00A03B55`
- [EtwTimLogRedirectionTrustPolicy](../../page/AB/EtwTimLogRedirectionTrustPolicy_function_00ABA7E0.md) at `0x00ABAA10`
- [EtwTimLogRedirectionTrustPolicy](../../page/AB/EtwTimLogRedirectionTrustPolicy_function_00ABA7E0.md) at `0x00ABAA95`
- [VfMiscMmUnmapLockedPages_Entry](../../pagevrfy/BA/VfMiscMmUnmapLockedPages_Entry_function_00BAE1D0.md) at `0x00BAE2FB`
- [VfMiscMmUnmapLockedPages_Entry](../../pagevrfy/BA/VfMiscMmUnmapLockedPages_Entry_function_00BAE1D0.md) at `0x00BAE382`
- [VfMiscMmUnmapLockedPages_Entry](../../pagevrfy/BA/VfMiscMmUnmapLockedPages_Entry_function_00BAE1D0.md) at `0x00BAE3BD`

### Static image references
- `0x006AD53C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006AD549` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006AD530  48 8B C4                        mov rax, rsp
006AD533  FA                              cli
006AD534  48 83 EC 10                     sub rsp, 0x10
006AD538  50                              push rax
006AD539  9C                              pushfq
006AD53A  6A 10                           push 0x10
006AD53C  48 8D 05 1D 5F 00 00            lea rax, [rip + 0x5f1d]
006AD543  50                              push rax
006AD544  B8 23 00 00 00                  mov eax, 0x23
006AD549  E9 72 74 01 00                  jmp 0x1406c49c0
006AD54E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwQueryVirtualMemory(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwQueryVirtualMemory(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AD530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AD530[BB_006AD530]
  bb_006AD54E[BB_006AD54E]
```
