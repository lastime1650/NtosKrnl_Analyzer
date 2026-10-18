# NtQueryDirectoryFileEx

- RVA: `0x008EC680`–`0x008EC761` (길이 `225` bytes)
- VA: `0x00000001408EC680`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00086C88`
- 디코드: `46`개 명령, `225/225` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008EC70F` → [BuildQueryDirectoryIrp](BuildQueryDirectoryIrp_function_008EC770.md) (function, `0x008EC770`)
- `0x008EC753` → [IopSynchronousServiceTail](IopSynchronousServiceTail_function_008EB440.md) (function, `0x008EB440`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008EC680  4C 8B DC                        mov r11, rsp
008EC683  48 81 EC A8 00 00 00            sub rsp, 0xa8
008EC68A  33 C0                           xor eax, eax
008EC68C  41 C6 43 D8 00                  mov byte ptr [r11 - 0x28], 0
008EC691  49 89 43 F0                     mov qword ptr [r11 - 0x10], rax
008EC695  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
008EC699  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
008EC69D  41 88 43 D9                     mov byte ptr [r11 - 0x27], al
008EC6A1  49 8D 43 D9                     lea rax, [r11 - 0x27]
008EC6A5  49 89 43 D0                     mov qword ptr [r11 - 0x30], rax
008EC6A9  49 8D 43 E0                     lea rax, [r11 - 0x20]
008EC6AD  49 89 43 C8                     mov qword ptr [r11 - 0x38], rax
008EC6B1  49 8D 43 E8                     lea rax, [r11 - 0x18]
008EC6B5  49 89 43 C0                     mov qword ptr [r11 - 0x40], rax
008EC6B9  49 8D 43 F0                     lea rax, [r11 - 0x10]
008EC6BD  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
008EC6C1  49 8D 43 D8                     lea rax, [r11 - 0x28]
008EC6C5  49 89 43 B0                     mov qword ptr [r11 - 0x50], rax
008EC6C9  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
008EC6D1  49 89 43 A0                     mov qword ptr [r11 - 0x60], rax
008EC6D5  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
008EC6DC  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008EC6E0  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
008EC6E7  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
008EC6EB  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
008EC6F2  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008EC6F6  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
008EC6FE  49 89 43 80                     mov qword ptr [r11 - 0x80], rax
008EC702  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
008EC70A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008EC70F  E8 5C 00 00 00                  call 0x1408ec770
008EC714  85 C0                           test eax, eax
008EC716  75 40                           jne 0x1408ec758
008EC718  0F B6 84 24 80 00 00 00         movzx eax, byte ptr [rsp + 0x80]
008EC720  41 B1 01                        mov r9b, 1
008EC723  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
008EC72B  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
008EC733  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
008EC73B  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
008EC743  88 44 24 28                     mov byte ptr [rsp + 0x28], al
008EC747  0F B6 84 24 81 00 00 00         movzx eax, byte ptr [rsp + 0x81]
008EC74F  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008EC753  E8 E8 EC FF FF                  call 0x1408eb440
008EC758  48 81 C4 A8 00 00 00            add rsp, 0xa8
008EC75F  C3                              ret
008EC760  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryDirectoryFileEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7, unsigned int a8, unsigned int a9, __int64 a10)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int8 v_stack_m27;
    unsigned __int8 v_stack_m28;
    unsigned int v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int8 v_stack_m80;
    unsigned __int64 v_stack_m88;

    v_rsp = (v_rsp) - (168);
    result = 0;
    *(unsigned __int8 *)(v_rsp - 40) = 0;
    *(unsigned __int64 *)(v_rsp - 16) = 0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    *(unsigned __int64 *)(v_rsp - 32) = 0;
    *(unsigned __int8 *)(v_rsp - 39) = 0;
    *(unsigned __int64 *)(v_rsp - 48) = v_rsp - 39;
    *(unsigned __int64 *)(v_rsp - 56) = v_rsp - 32;
    *(unsigned __int64 *)(v_rsp - 64) = v_rsp - 24;
    *(unsigned __int64 *)(v_rsp - 72) = v_rsp - 16;
    *(unsigned __int64 *)(v_rsp - 80) = v_rsp - 40;
    *(unsigned __int64 *)(v_rsp - 96) = a10;
    v_stack_m68 = (unsigned int)((unsigned int)(a9));
    v_stack_m70 = (unsigned int)((unsigned int)(a8));
    v_stack_m78 = (unsigned int)((unsigned int)(a7));
    *(unsigned __int64 *)(v_rsp - 128) = a6;
    v_stack_m88 = a5;
    result = BuildQueryDirectoryIrp(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) {
        result = v_stack_m28;
        a4 = 1;
        a3 = v_stack_m20;
        a2 = v_stack_m18;
        a1 = v_stack_m10;
        v_stack_m78 = 2;
        v_stack_m80 = (unsigned __int8)(result);
        result = v_stack_m27;
        v_stack_m88 = (unsigned __int8)(result);
        result = IopSynchronousServiceTail(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (168);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryDirectoryFileEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint8_t v_stack_m27;
    uint8_t v_stack_m28;
    uint32_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m78;
    uint8_t v_stack_m80;
    uint64_t v_stack_m88;

    local_rsp = (local_rsp) - (168);
    result = 0;
    *(uint8_t *)(local_rsp - 0x28) = 0;
    *(uint64_t *)(local_rsp - 0x10) = 0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    *(uint64_t *)(local_rsp - 0x20) = 0;
    *(uint8_t *)(local_rsp - 0x27) = 0;
    *(uint64_t *)(local_rsp - 0x30) = local_rsp - 39;
    *(uint64_t *)(local_rsp - 0x38) = local_rsp - 32;
    *(uint64_t *)(local_rsp - 0x40) = local_rsp - 24;
    *(uint64_t *)(local_rsp - 0x48) = local_rsp - 16;
    *(uint64_t *)(local_rsp - 0x50) = local_rsp - 40;
    *(uint64_t *)(local_rsp - 0x60) = Arg10;
    v_stack_m68 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m70 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m78 = (uint32_t)((uint32_t)(Arg7));
    *(uint64_t *)(local_rsp - 0x80) = Arg6;
    v_stack_m88 = Arg5;
    result = BuildQueryDirectoryIrp(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) {
        result = v_stack_m28;
        Arg4 = 1;
        Arg3 = v_stack_m20;
        Arg2 = v_stack_m18;
        Arg1 = v_stack_m10;
        v_stack_m78 = 2;
        v_stack_m80 = (uint8_t)(result);
        result = v_stack_m27;
        v_stack_m88 = (uint8_t)(result);
        result = IopSynchronousServiceTail(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (168);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008EC680&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008EC680[BB_008EC680]
  bb_008EC718[BB_008EC718]
  bb_008EC758[BB_008EC758]
  bb_008EC760[BB_008EC760]
  bb_008EC680 -->|branch| bb_008EC758
  bb_008EC680 -->|fallthrough| bb_008EC718
  bb_008EC718 -->|flow| bb_008EC758
```
