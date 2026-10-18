# sub_00B1EB18

- RVA: `0x00B1EB18`–`0x00B1EBD6` (길이 `190` bytes)
- VA: `0x0000000140B1EB18`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000878E8`
- 디코드: `45`개 명령, `190/190` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B1EB35` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B1EB44` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B1EB50` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B1EB6B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B1EB83` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B1EBAF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x00B1EBCB` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **7**
  - `0x00B1EB35` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B1EB44` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B1EB50` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B1EB6B` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B1EB83` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B1EBAF` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
  - `0x00B1EBCB` → [IoAddTriageDumpDataBlock](../../text/42/IoAddTriageDumpDataBlock_function_00428374.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00B1EB26` → [IoSetDevicePropertyData + 0x95](../8F/IoSetDevicePropertyData_function_008F6010.md) (`tail-transfer`)
  - `0x00B1EB9A` → [IoSetDevicePropertyData + 0x95](../8F/IoSetDevicePropertyData_function_008F6010.md) (`tail-transfer`)
  - `0x00B1EBA7` → [IoSetDevicePropertyData + 0x95](../8F/IoSetDevicePropertyData_function_008F6010.md) (`tail-transfer`)
  - `0x00B1EBD1` → [IoSetDevicePropertyData + 0x95](../8F/IoSetDevicePropertyData_function_008F6010.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B1EB18  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
00B1EB1F  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B1EB23  48 85 C9                        test rcx, rcx
00B1EB26  0F 84 79 75 DD FF               je 0x1408f60a5
00B1EB2C  BA 88 03 00 00                  mov edx, 0x388
00B1EB31  48 8D 79 28                     lea rdi, [rcx + 0x28]
00B1EB35  E8 3A 98 90 FF                  call 0x140428374
00B1EB3A  66 39 37                        cmp word ptr [rdi], si
00B1EB3D  74 16                           je 0x140b1eb55
00B1EB3F  8B D5                           mov edx, ebp
00B1EB41  48 8B CF                        mov rcx, rdi
00B1EB44  E8 2B 98 90 FF                  call 0x140428374
00B1EB49  0F B7 17                        movzx edx, word ptr [rdi]
00B1EB4C  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
00B1EB50  E8 1F 98 90 FF                  call 0x140428374
00B1EB55  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
00B1EB5C  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B1EB60  48 83 C1 38                     add rcx, 0x38
00B1EB64  66 39 31                        cmp word ptr [rcx], si
00B1EB67  74 1F                           je 0x140b1eb88
00B1EB69  8B D5                           mov edx, ebp
00B1EB6B  E8 04 98 90 FF                  call 0x140428374
00B1EB70  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
00B1EB77  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B1EB7B  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B1EB7F  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B1EB83  E8 EC 97 90 FF                  call 0x140428374
00B1EB88  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
00B1EB8F  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B1EB93  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00B1EB97  48 85 C0                        test rax, rax
00B1EB9A  0F 84 05 75 DD FF               je 0x1408f60a5
00B1EBA0  48 8D 48 38                     lea rcx, [rax + 0x38]
00B1EBA4  66 39 31                        cmp word ptr [rcx], si
00B1EBA7  0F 84 F8 74 DD FF               je 0x1408f60a5
00B1EBAD  8B D5                           mov edx, ebp
00B1EBAF  E8 C0 97 90 FF                  call 0x140428374
00B1EBB4  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
00B1EBBB  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
00B1EBBF  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
00B1EBC3  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
00B1EBC7  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
00B1EBCB  E8 A4 97 90 FF                  call 0x140428374
00B1EBD0  90                              nop
00B1EBD1  E9 CF 74 DD FF                  jmp 0x1408f60a5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B1EB18(void)
{
    __int64 result;

    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40), 904, a3, a4);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40)) != ((unsigned __int16)(v_rsi))) {
        a2 = (unsigned int)(v_rbp);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40 + 8);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40)) + (56);
    result = *(unsigned __int64 *)(v_rbx + 312);
    if ((*(unsigned __int16 *)(a1)) != ((unsigned __int16)(v_rsi))) {
        a2 = (unsigned int)(v_rbp);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(v_rbx + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 16) + 56, (unsigned int)((unsigned int)(v_rbp)), a3, a4);
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 16) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 16) + 56), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_00B1EB18(void)
{
    int64_t result;

    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28), 904, a3, a4);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x28)) != ((uint16_t)(local_rsi))) {
        a2 = (uint32_t)(local_rbp);
        a1 = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x28);
        a1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x28 + 0x8);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    a1 = (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28)) + (56);
    result = *(uint64_t *)(local_rbx + 0x138);
    if ((*(uint16_t *)(a1)) != ((uint16_t)(local_rsi))) {
        a2 = (uint32_t)(local_rbp);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        result = *(uint64_t *)(local_rbx + 0x138);
        a1 = *(uint64_t *)(result + 0x28);
        a2 = *(uint16_t *)(a1 + 0x38);
        a1 = *(uint64_t *)(a1 + 0x40);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x10) + 56, (uint32_t)((uint32_t)(local_rbp)), a3, a4);
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x10) + 0x40), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x10) + 0x38), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1EB18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1EB18[BB_00B1EB18]
  bb_00B1EB2C[BB_00B1EB2C]
  bb_00B1EB3F[BB_00B1EB3F]
  bb_00B1EB55[BB_00B1EB55]
  bb_00B1EB69[BB_00B1EB69]
  bb_00B1EB88[BB_00B1EB88]
  bb_00B1EBA0[BB_00B1EBA0]
  bb_00B1EBAD[BB_00B1EBAD]
  bb_00B1EB18 -->|fallthrough| bb_00B1EB2C
  bb_00B1EB2C -->|branch| bb_00B1EB55
  bb_00B1EB2C -->|fallthrough| bb_00B1EB3F
  bb_00B1EB3F -->|flow| bb_00B1EB55
  bb_00B1EB55 -->|branch| bb_00B1EB88
  bb_00B1EB55 -->|fallthrough| bb_00B1EB69
  bb_00B1EB69 -->|flow| bb_00B1EB88
  bb_00B1EB88 -->|fallthrough| bb_00B1EBA0
  bb_00B1EBA0 -->|fallthrough| bb_00B1EBAD
```
