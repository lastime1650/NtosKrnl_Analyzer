# SysCtxOpenEffectiveToken

- RVA: `0x00ACEED8`–`0x00ACEF21` (길이 `73` bytes)
- VA: `0x0000000140ACEED8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C80`
- 디코드: `20`개 명령, `73/73` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00ACEEF7` → [ZwOpenThreadTokenEx](../../text/6A/ZwOpenThreadTokenEx_function_006AD6B0.md) (function, `0x006AD6B0`)
- `0x00ACEF15` → [ZwOpenProcessTokenEx](../../text/6A/ZwOpenProcessTokenEx_function_006AD6D0.md) (function, `0x006AD6D0`)

### Direct callers
- [SysCtxRegOpenCurrentUserKey](../8F/SysCtxRegOpenCurrentUserKey_function_008F455C.md) at `0x008F45CA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00ACEEF7` → [ZwOpenThreadTokenEx](../../text/6A/ZwOpenThreadTokenEx_function_006AD6B0.md) (`PAGE` → `.text`)
  - `0x00ACEF15` → [ZwOpenProcessTokenEx](../../text/6A/ZwOpenProcessTokenEx_function_006AD6D0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACEED8  40 53                           push rbx
00ACEEDA  48 83 EC 30                     sub rsp, 0x30
00ACEEDE  45 33 C0                        xor r8d, r8d
00ACEEE1  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
00ACEEE6  48 8B DA                        mov rbx, rdx
00ACEEE9  41 B9 00 02 00 00               mov r9d, 0x200
00ACEEEF  41 8D 50 08                     lea edx, [r8 + 8]
00ACEEF3  49 8D 48 FE                     lea rcx, [r8 - 2]
00ACEEF7  E8 B4 E7 BD FF                  call 0x1406ad6b0
00ACEEFC  3D 7C 00 00 C0                  cmp eax, 0xc000007c
00ACEF01  75 17                           jne 0x140acef1a
00ACEF03  4C 8B CB                        mov r9, rbx
00ACEF06  BA 08 00 00 00                  mov edx, 8
00ACEF0B  41 B8 00 02 00 00               mov r8d, 0x200
00ACEF11  48 83 C9 FF                     or rcx, 0xffffffffffffffff
00ACEF15  E8 B6 E7 BD FF                  call 0x1406ad6d0
00ACEF1A  48 83 C4 30                     add rsp, 0x30
00ACEF1E  5B                              pop rbx
00ACEF1F  C3                              ret
00ACEF20  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SysCtxOpenEffectiveToken(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (48);
    a3 = 0;
    v_stack_m18 = a2;
    result = ZwOpenThreadTokenEx(a3 - 2, a3 + 8, a3, 512);
    if (((unsigned int)(result)) == 0xC000007CULL) {
        a4 = a2;
        a2 = 8;
        a3 = 512;
        a1 = (a3 - 2) | (-1);
        result = ZwOpenProcessTokenEx(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SysCtxOpenEffectiveToken(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (48);
    Arg3 = 0;
    v_stack_m18 = Arg2;
    result = ZwOpenThreadTokenEx(Arg3 - 2, Arg3 + 8, Arg3, 512);
    if (((uint32_t)(result)) == 0xC000007CULL) {
        a4 = Arg2;
        Arg2 = 8;
        Arg3 = 512;
        Arg1 = (Arg3 - 2) | (-1);
        result = ZwOpenProcessTokenEx(Arg1, Arg2, Arg3, a4);
    }
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACEED8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ACEED8[BB_00ACEED8]
  bb_00ACEF03[BB_00ACEF03]
  bb_00ACEF1A[BB_00ACEF1A]
  bb_00ACEF20[BB_00ACEF20]
  bb_00ACEED8 -->|branch| bb_00ACEF1A
  bb_00ACEED8 -->|fallthrough| bb_00ACEF03
  bb_00ACEF03 -->|flow| bb_00ACEF1A
```
