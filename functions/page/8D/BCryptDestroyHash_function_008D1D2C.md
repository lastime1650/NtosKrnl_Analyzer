# BCryptDestroyHash

- RVA: `0x008D1D2C`–`0x008D1D77` (길이 `75` bytes)
- VA: `0x00000001408D1D2C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `21`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008D1D45` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x008D1D56` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008D1D64` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)

### Direct callers
- [sub_008D1E14](Unknown_function_008D1E14.md) at `0x008D1F53`
- [RtlGenerateClass5Guid](../AC/RtlGenerateClass5Guid_function_00AC4510.md) at `0x00AC46D7`

### Static image references
- `0x008D1D3E` → RVA `0x00F04E30` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x008D1D45` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x008D1D56` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008D1D64` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008D1D2C  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008D1D31  57                              push rdi
008D1D32  48 83 EC 20                     sub rsp, 0x20
008D1D36  48 8B F9                        mov rdi, rcx
008D1D39  BB 02 00 00 C0                  mov ebx, 0xc0000002
008D1D3E  48 8B 0D EB 30 63 00            mov rcx, qword ptr [rip + 0x6330eb]
008D1D45  E8 CA 6A B5 FF                  call 0x140428814
008D1D4A  48 85 C0                        test rax, rax
008D1D4D  74 1A                           je 0x1408d1d69
008D1D4F  48 8B 40 38                     mov rax, qword ptr [rax + 0x38]
008D1D53  48 8B CF                        mov rcx, rdi
008D1D56  E8 75 8D DE FF                  call 0x1406baad0
008D1D5B  48 8B 0D CE 30 63 00            mov rcx, qword ptr [rip + 0x6330ce]
008D1D62  8B D8                           mov ebx, eax
008D1D64  E8 57 50 B8 FF                  call 0x140456dc0
008D1D69  8B C3                           mov eax, ebx
008D1D6B  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008D1D70  48 83 C4 20                     add rsp, 0x20
008D1D74  5F                              pop rdi
008D1D75  C3                              ret
008D1D76  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BCryptDestroyHash(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    result = ExGetExtensionTable(*(unsigned __int64 *)(v_rip + 6500587), a2, a3, a4);
    v_rbx = (unsigned int)(0xC0000002ULL);
    if (result != 0) {
        result = *(unsigned __int64 *)(result + 56);
        a1 = a1;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 6500558);
        v_rbx = (unsigned int)(result);
        result = ExReleaseExtensionTable(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t BCryptDestroyHash(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    result = ExGetExtensionTable(*(uint64_t *)(v_rip + 0x6330EB), a2, a3, a4);
    local_rbx = (uint32_t)(0xC0000002ULL);
    if (result != 0) {
        result = *(uint64_t *)(result + 0x38);
        Arg1 = Arg1;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
        Arg1 = *(uint64_t *)(v_rip + 0x6330CE);
        local_rbx = (uint32_t)(result);
        result = ExReleaseExtensionTable(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008D1D2C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008D1D2C[BB_008D1D2C]
  bb_008D1D4F[BB_008D1D4F]
  bb_008D1D69[BB_008D1D69]
  bb_008D1D76[BB_008D1D76]
  bb_008D1D2C -->|branch| bb_008D1D69
  bb_008D1D2C -->|fallthrough| bb_008D1D4F
  bb_008D1D4F -->|flow| bb_008D1D69
```
