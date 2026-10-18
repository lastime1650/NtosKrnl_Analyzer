# SeCompareSigningLevels

- RVA: `0x00A13760`–`0x00A13780` (길이 `32` bytes)
- VA: `0x0000000140A13760`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A13775` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [MiCreateSystemSection](../../text/45/MiCreateSystemSection_function_00453158.md) at `0x004532D2`
- [MiWriteSegmentSignatureFlags](../../text/4B/MiWriteSegmentSignatureFlags_function_004B78C4.md) at `0x004B78ED`
- [MiWriteSegmentSignatureFlags](../../text/4B/MiWriteSegmentSignatureFlags_function_004B78C4.md) at `0x004B7921`
- [PsCheckProcessFileSigningLevel](../78/PsCheckProcessFileSigningLevel_function_00783800.md) at `0x0078386C`
- [PsCheckProcessFileSigningLevel](../78/PsCheckProcessFileSigningLevel_function_00783800.md) at `0x007839FA`
- [MiApplyImageHotPatchRequest](../80/MiApplyImageHotPatchRequest_function_008025AC.md) at `0x008028ED`
- [MiValidateSectionSigningPolicy](../93/MiValidateSectionSigningPolicy_function_0093FF40.md) at `0x0094007C`
- [MiValidateExistingImage](../98/MiValidateExistingImage_function_009864B4.md) at `0x0098669B`
- [MiValidateExistingImage](../98/MiValidateExistingImage_function_009864B4.md) at `0x009866BD`
- [SepIsImageInMinTcbList](SepIsImageInMinTcbList_function_00A12DE0.md) at `0x00A12EAC`
- [SepIsImageInMinTcbList](SepIsImageInMinTcbList_function_00A12DE0.md) at `0x00A12EBB`
- [SeQuerySigningPolicy](SeQuerySigningPolicy_function_00A12F44.md) at `0x00A1308E`
- [SepIsMinTCB](SepIsMinTCB_function_00A13120.md) at `0x00A13348`
- [SepIsMinTCB](SepIsMinTCB_function_00A13120.md) at `0x00A1335A`
- [SepCheckAndSetAuditModeForProcess](SepCheckAndSetAuditModeForProcess_function_00A134FC.md) at `0x00A1358D`
- [SeGetImageRequiredSigningLevel](SeGetImageRequiredSigningLevel_function_00A135BC.md) at `0x00A13663`
- [PsConvertToGuiThread](../A2/PsConvertToGuiThread_function_00A2F8B0.md) at `0x00A2FA4A`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEAB77`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEAFE5`
- [sub_00B29218](../B2/Unknown_function_00B29218.md) at `0x00B293F4`
- [sub_00B36D9A](../B3/Unknown_function_00B36D9A.md) at `0x00B36D9F`
- [sub_00B36D9A](../B3/Unknown_function_00B36D9A.md) at `0x00B36DC6`

### Static image references
- `0x00A13764` → RVA `0x00F04E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A13775` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A13760  48 83 EC 28                     sub rsp, 0x28
00A13764  4C 8B 05 15 17 4F 00            mov r8, qword ptr [rip + 0x4f1715]
00A1376B  33 C0                           xor eax, eax
00A1376D  4D 85 C0                        test r8, r8
00A13770  74 08                           je 0x140a1377a
00A13772  49 8B C0                        mov rax, r8
00A13775  E8 56 73 CA FF                  call 0x1406baad0
00A1377A  48 83 C4 28                     add rsp, 0x28
00A1377E  C3                              ret
00A1377F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeCompareSigningLevels(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (*(unsigned __int64 *)(v_rip + 5183253) != 0) {
        result = *(unsigned __int64 *)(v_rip + 5183253);
        result = guard_dispatch_icall(a1, a2, *(unsigned __int64 *)(v_rip + 5183253), a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void SeCompareSigningLevels(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (*(uint64_t *)(v_rip + 0x4F1715) != 0) {
        result = *(uint64_t *)(v_rip + 0x4F1715);
        result = guard_dispatch_icall(a1, a2, *(uint64_t *)(v_rip + 0x4F1715), a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A13760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A13760[BB_00A13760]
  bb_00A13772[BB_00A13772]
  bb_00A1377A[BB_00A1377A]
  bb_00A1377F[BB_00A1377F]
  bb_00A13760 -->|branch| bb_00A1377A
  bb_00A13760 -->|fallthrough| bb_00A13772
  bb_00A13772 -->|flow| bb_00A1377A
```
