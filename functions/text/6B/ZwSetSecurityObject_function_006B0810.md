# ZwSetSecurityObject

- RVA: `0x006B0810`–`0x006B082F` (길이 `31` bytes)
- VA: `0x00000001406B0810`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C1348`
- 디코드: `11`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [BiZwSetSecurityObject](../4A/BiZwSetSecurityObject_function_004A9A84.md) at `0x004A9A8D`
- [DifZwSetSecurityObjectWrapper](../64/DifZwSetSecurityObjectWrapper_function_0064ADF0.md) at `0x0064AED3`
- [CmpApplyAdminSdOnHiveFiles](../66/CmpApplyAdminSdOnHiveFiles_function_0066A168.md) at `0x0066A190`
- [CmpApplyAdminSdOnHiveFiles](../66/CmpApplyAdminSdOnHiveFiles_function_0066A168.md) at `0x0066A1CD`
- [CmpApplyAdminSdOnHiveFiles](../66/CmpApplyAdminSdOnHiveFiles_function_0066A168.md) at `0x0066A1EA`
- [CmpApplyAdminSdOnHiveFiles](../66/CmpApplyAdminSdOnHiveFiles_function_0066A168.md) at `0x0066A207`
- [SmKmStoreFileCreateForIoType](../../page/7A/SmKmStoreFileCreateForIoType_function_007A93C8.md) at `0x007A9582`
- [CmpDoReDoRecord](../../page/7F/CmpDoReDoRecord_function_007F76B8.md) at `0x007F7783`
- [MiCreatePagingFile](../../page/7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF529`
- [RegRtlSetKeySecurity](../../page/83/RegRtlSetKeySecurity_function_00832CDC.md) at `0x00832CE0`
- [PiDevCfgCopyDeviceKeys](../../page/99/PiDevCfgCopyDeviceKeys_function_00995E1C.md) at `0x00995F6E`
- [PiDevCfgCopyDeviceKey](../../page/99/PiDevCfgCopyDeviceKey_function_00997374.md) at `0x00997ADE`
- [sub_00B2C5F4](../../page/B2/Unknown_function_00B2C5F4.md) at `0x00B2CA63`
- [IopApplySystemPartitionProt](../../init/C2/IopApplySystemPartitionProt_function_00C2E398.md) at `0x00C2E5A0`

### Static image references
- `0x006B081C` → RVA `0x006B3460` (`KiServiceLinkage`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006B0829` → [KiServiceInternal](../6C/KiServiceInternal_function_006C49C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006B0810  48 8B C4                        mov rax, rsp
006B0813  FA                              cli
006B0814  48 83 EC 10                     sub rsp, 0x10
006B0818  50                              push rax
006B0819  9C                              pushfq
006B081A  6A 10                           push 0x10
006B081C  48 8D 05 3D 2C 00 00            lea rax, [rip + 0x2c3d]
006B0823  50                              push rax
006B0824  B8 BA 01 00 00                  mov eax, 0x1ba
006B0829  E9 92 41 01 00                  jmp 0x1406c49c0
006B082E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ZwSetSecurityObject(void)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (16);
}
```

## 5. (Beta) C Style

```c
void ZwSetSecurityObject(void)
{
    int64_t local_rsp;

    local_rsp = (local_rsp) - (16);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006B0810&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006B0810[BB_006B0810]
  bb_006B082E[BB_006B082E]
```
