# SepFinalizeTokenAcls

- RVA: `0x008B63F4`–`0x008B6423` (길이 `47` bytes)
- VA: `0x00000001408B63F4`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064CA8`
- 디코드: `15`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008B6409` → [SepAppendAceToTokenObjectAcl](SepAppendAceToTokenObjectAcl_function_008B6430.md) (function, `0x008B6430`)
- `0x008B641C` → [SepSetProcessTrustLabelAceForToken](../../text/40/SepSetProcessTrustLabelAceForToken_function_004007A0.md) (function, `0x004007A0`)

### Direct callers
- [SepCreateTokenEx](../../text/4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004EA8CD`
- [SepCreateTokenEx](../../text/4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004EA91F`
- [SepCreateAppContainerToken](../../text/4F/SepCreateAppContainerToken_function_004F43AC.md) at `0x004F4C88`
- [SeFilterToken](../79/SeFilterToken_function_0079CD00.md) at `0x0079CE06`
- [sub_00891F9F](../89/Unknown_function_00891F9F.md) at `0x00892009`
- [PsImpersonateClient](../8C/PsImpersonateClient_function_008CBE10.md) at `0x008CC30C`
- [NtFilterToken](../9C/NtFilterToken_function_009C7890.md) at `0x009C7B9D`
- [SepCopyAnonymousTokenAndSetSilo](../A3/SepCopyAnonymousTokenAndSetSilo_function_00A3A510.md) at `0x00A3A642`
- [SeSubProcessToken](../AA/SeSubProcessToken_function_00AAD570.md) at `0x00AADDCB`
- [NtCreateLowBoxToken](../AB/NtCreateLowBoxToken_function_00AB9880.md) at `0x00ABA30A`

### Static image references
- `0x008B63FA` → RVA `0x00FD9A68` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008B641C` → [SepSetProcessTrustLabelAceForToken](../../text/40/SepSetProcessTrustLabelAceForToken_function_004007A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B63F4  40 53                           push rbx
008B63F6  48 83 EC 20                     sub rsp, 0x20
008B63FA  4C 8B 05 67 36 72 00            mov r8, qword ptr [rip + 0x723667]
008B6401  BA 08 00 00 00                  mov edx, 8
008B6406  48 8B D9                        mov rbx, rcx
008B6409  E8 22 00 00 00                  call 0x1408b6430
008B640E  85 C0                           test eax, eax
008B6410  79 07                           jns 0x1408b6419
008B6412  48 83 C4 20                     add rsp, 0x20
008B6416  5B                              pop rbx
008B6417  C3                              ret
008B6418  CC                              int3
008B6419  48 8B CB                        mov rcx, rbx
008B641C  E8 7F A3 B4 FF                  call 0x1404007a0
008B6421  EB EF                           jmp 0x1408b6412
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepFinalizeTokenAcls(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = SepAppendAceToTokenObjectAcl(a1, 8, *(unsigned __int64 *)(v_rip + 7485031), a4);
    if (!sign_flag) goto loc_008B6419;
loc_008B6412:
    v_rsp = (v_rsp) + (32);
    return result;
loc_008B6419:
    result = SepSetProcessTrustLabelAceForToken(a1, 8, *(unsigned __int64 *)(v_rip + 7485031), a4);
    goto loc_008B6412;
}
```

## 5. (Beta) C Style

```c
int64_t SepFinalizeTokenAcls(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = SepAppendAceToTokenObjectAcl(Arg1, 8, *(uint64_t *)(v_rip + 0x723667), a4);
    if (!sign_flag) goto loc_008B6419;
loc_008B6412:
    local_rsp = (local_rsp) + (32);
    return result;
loc_008B6419:
    result = SepSetProcessTrustLabelAceForToken(Arg1, 8, *(uint64_t *)(v_rip + 0x723667), a4);
    goto loc_008B6412;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B63F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008B63F4[BB_008B63F4]
  bb_008B6412[BB_008B6412]
  bb_008B6418[BB_008B6418]
  bb_008B6419[BB_008B6419]
  bb_008B63F4 -->|branch| bb_008B6419
  bb_008B63F4 -->|fallthrough| bb_008B6412
  bb_008B6418 -->|flow| bb_008B6419
  bb_008B6419 -->|branch| bb_008B6412
```
