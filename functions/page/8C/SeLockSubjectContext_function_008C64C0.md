# SeLockSubjectContext

- RVA: `0x008C64C0`–`0x008C6515` (길이 `85` bytes)
- VA: `0x00000001408C64C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `23`개 명령, `85/85` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **17**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008C64E4` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008C6509` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)

### Direct callers
- [IopCreateSecurityCheck](../../text/3A/IopCreateSecurityCheck_function_003A5DA0.md) at `0x003A5DFF`
- [SeAccessCheckWithHint](../../text/3A/SeAccessCheckWithHint_function_003A6C30.md) at `0x003A6D86`
- [SepTrustLevelCheck](../../text/3E/SepTrustLevelCheck_function_003ED7E0.md) at `0x003EDA1B`
- [SepCommonAccessCheckEx](../../text/47/SepCommonAccessCheckEx_function_0047602C.md) at `0x004762B2`
- [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F48B3`
- [SeAdjustAntiTamperCreatorAccess](../../text/60/SeAdjustAntiTamperCreatorAccess_function_00607590.md) at `0x00607646`
- [SepMandatoryAccessCheck](../../text/60/SepMandatoryAccessCheck_function_00608480.md) at `0x00608538`
- [CMFCheckAccess](../7D/CMFCheckAccess_function_007D28B4.md) at `0x007D29ED`
- [IopParseDevice](../89/IopParseDevice_function_0089E510.md) at `0x0089EA9E`
- [IopParseDevice](../89/IopParseDevice_function_0089E510.md) at `0x008A0037`
- [IopParseDevice](../89/IopParseDevice_function_0089E510.md) at `0x008A0382`
- [ObpCheckObjectReference](ObpCheckObjectReference_function_008C6084.md) at `0x008C60FC`
- [ObCheckCreateObjectAccess](ObCheckCreateObjectAccess_function_008C6340.md) at `0x008C63C1`
- [ObpCheckTraverseAccess](ObpCheckTraverseAccess_function_008C6CE4.md) at `0x008C6D7E`
- [CmpCheckCreateAccess](CmpCheckCreateAccess_function_008C6E8C.md) at `0x008C6EBC`
- [ObpVerifyCreatorAccessCheck](../9C/ObpVerifyCreatorAccessCheck_function_009CA524.md) at `0x009CA603`
- [EtwpCoverageUserIsAdmin](../9F/EtwpCoverageUserIsAdmin_function_009FE548.md) at `0x009FE56A`
- [SepAccessCheckAndAuditAlarm](../A1/SepAccessCheckAndAuditAlarm_function_00A1AF4C.md) at `0x00A1BA67`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF1C06`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008C64E4` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008C6509` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008C64C0  40 53                           push rbx
008C64C2  48 83 EC 20                     sub rsp, 0x20
008C64C6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C64CF  48 8B D9                        mov rbx, rcx
008C64D2  B2 01                           mov dl, 1
008C64D4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008C64DB  90                              nop
008C64DC  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
008C64E0  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008C64E4  E8 D7 B6 94 FF                  call 0x140211bc0
008C64E9  48 83 3B 00                     cmp qword ptr [rbx], 0
008C64ED  74 1F                           je 0x1408c650e
008C64EF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C64F8  B2 01                           mov dl, 1
008C64FA  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008C6501  90                              nop
008C6502  48 8B 0B                        mov rcx, qword ptr [rbx]
008C6505  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008C6509  E8 B2 B6 94 FF                  call 0x140211bc0
008C650E  48 83 C4 20                     add rsp, 0x20
008C6512  5B                              pop rbx
008C6513  C3                              ret
008C6514  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeLockSubjectContext(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 48), 1, a3, a4);
    if ((*(unsigned __int64 *)(a1)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = *(unsigned __int64 *)(a1);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ExAcquireResourceSharedLite(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeLockSubjectContext(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x30), 1, a3, a4);
    if ((*(uint64_t *)(arg1)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        a2 = 1;
        Arg1 = *(uint64_t *)(arg1);
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C64C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C64C0[BB_008C64C0]
  bb_008C64EF[BB_008C64EF]
  bb_008C650E[BB_008C650E]
  bb_008C6514[BB_008C6514]
  bb_008C64C0 -->|branch| bb_008C650E
  bb_008C64C0 -->|fallthrough| bb_008C64EF
  bb_008C64EF -->|flow| bb_008C650E
```
