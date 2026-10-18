# SepStopReferencingLogonSession

- RVA: `0x00A8E35C`–`0x00A8E395` (길이 `57` bytes)
- VA: `0x0000000140A8E35C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `17`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A8E369` → [SepConvertToOwnTokenClaims](../../text/4B/SepConvertToOwnTokenClaims_function_004B0AA0.md) (function, `0x004B0AA0`)
- `0x00A8E37B` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (function, `0x0044EDCC`)

### Direct callers
- [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) at `0x004AAFD3`
- [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) at `0x004AB0DF`
- [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x00606B7E`
- [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x00606B9B`
- [SepFilterToken](../9C/SepFilterToken_function_009C6B80.md) at `0x009C74ED`
- [NtSetInformationToken](../AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0D7D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A8E369` → [SepConvertToOwnTokenClaims](../../text/4B/SepConvertToOwnTokenClaims_function_004B0AA0.md) (`PAGE` → `.text`)
  - `0x00A8E37B` → [SepDeReferenceLogonSessionDirect](../../text/44/SepDeReferenceLogonSessionDirect_function_0044EDCC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A8E35C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A8E361  57                              push rdi
00A8E362  48 83 EC 20                     sub rsp, 0x20
00A8E366  48 8B D9                        mov rbx, rcx
00A8E369  E8 32 27 A2 FF                  call 0x1404b0aa0
00A8E36E  8B F8                           mov edi, eax
00A8E370  85 C0                           test eax, eax
00A8E372  78 15                           js 0x140a8e389
00A8E374  48 8B 8B D8 00 00 00            mov rcx, qword ptr [rbx + 0xd8]
00A8E37B  E8 4C 0A 9C FF                  call 0x14044edcc
00A8E380  83 8B C8 00 00 00 20            or dword ptr [rbx + 0xc8], 0x20
00A8E387  8B C7                           mov eax, edi
00A8E389  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A8E38E  48 83 C4 20                     add rsp, 0x20
00A8E392  5F                              pop rdi
00A8E393  C3                              ret
00A8E394  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepStopReferencingLogonSession(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = SepConvertToOwnTokenClaims(a1, a2, a3, a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(a1 + 216);
        result = SepDeReferenceLogonSessionDirect(a1, a2, a3, a4);
        result = (unsigned int)((unsigned int)((unsigned int)(result)));
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepStopReferencingLogonSession(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = SepConvertToOwnTokenClaims(Arg1, a2, a3, a4);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(arg1 + 0xD8);
        result = SepDeReferenceLogonSessionDirect(Arg1, a2, a3, a4);
        result = (uint32_t)((uint32_t)((uint32_t)(result)));
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC8` | `32` | `R/W` |
| `Arg1` | `+ 0xD8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A8E35C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A8E35C[BB_00A8E35C]
  bb_00A8E374[BB_00A8E374]
  bb_00A8E389[BB_00A8E389]
  bb_00A8E394[BB_00A8E394]
  bb_00A8E35C -->|branch| bb_00A8E389
  bb_00A8E35C -->|fallthrough| bb_00A8E374
  bb_00A8E374 -->|flow| bb_00A8E389
```
