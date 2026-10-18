# SepReferenceLogonSession

- RVA: `0x00A3B74C`–`0x00A3B77B` (길이 `47` bytes)
- VA: `0x0000000140A3B74C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `15`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A3B75C` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x00A3B76A` → [SepReferenceLogonSessionSilo](SepReferenceLogonSessionSilo_function_00A3B784.md) (function, `0x00A3B784`)

### Direct callers
- [SepDuplicateLogonSessionReference](../../text/44/SepDuplicateLogonSessionReference_function_004463B0.md) at `0x00446402`
- [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) at `0x004AB046`
- [SepCreateTokenEx](../../text/4E/SepCreateTokenEx_function_004E9CD0.md) at `0x004EA4CA`
- [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) at `0x00606A83`
- [SepDuplicateToken](../8B/SepDuplicateToken_function_008B87EC.md) at `0x008B8C54`
- [SepFilterToken](../9C/SepFilterToken_function_009C6B80.md) at `0x009C70CE`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AED71A`
- [NtQueryInformationToken](../AE/NtQueryInformationToken_function_00AECDD0.md) at `0x00AEE70C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A3B75C` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A3B74C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00A3B751  57                              push rdi
00A3B752  48 83 EC 20                     sub rsp, 0x20
00A3B756  48 8B DA                        mov rbx, rdx
00A3B759  48 8B F9                        mov rdi, rcx
00A3B75C  E8 AF 9F 7E FF                  call 0x140225710
00A3B761  48 8B D0                        mov rdx, rax
00A3B764  4C 8B C3                        mov r8, rbx
00A3B767  48 8B CF                        mov rcx, rdi
00A3B76A  E8 15 00 00 00                  call 0x140a3b784
00A3B76F  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00A3B774  48 83 C4 20                     add rsp, 0x20
00A3B778  5F                              pop rdi
00A3B779  C3                              ret
00A3B77A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepReferenceLogonSession(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = PsGetCurrentServerSilo(a1, a2, a3, a4);
    result = SepReferenceLogonSessionSilo(a1, result, a2, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepReferenceLogonSession(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = PsGetCurrentServerSilo(Arg1, Arg2, a3, a4);
    result = SepReferenceLogonSessionSilo(Arg1, result, Arg2, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A3B74C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A3B74C[BB_00A3B74C]
  bb_00A3B77A[BB_00A3B77A]
```
