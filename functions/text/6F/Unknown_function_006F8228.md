# sub_006F8228

- RVA: `0x006F8228`–`0x006F82E9` (길이 `193` bytes)
- VA: `0x00000001406F8228`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B507C`
- 디코드: `45`개 명령, `193/193` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F8245` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x006F8255` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x006F8261` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x006F827D` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x006F8295` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x006F82C2` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)
- `0x006F82DE` → [IoAddTriageDumpDataBlock](../42/IoAddTriageDumpDataBlock_function_00428374.md) (function, `0x00428374`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x006F8236` → [IopQueueInvalidateBusRelationsRequest + 0x2B](../49/IopQueueInvalidateBusRelationsRequest_function_0049E28C.md) (`tail-transfer`)
  - `0x006F82AC` → [IopQueueInvalidateBusRelationsRequest + 0x2B](../49/IopQueueInvalidateBusRelationsRequest_function_0049E28C.md) (`tail-transfer`)
  - `0x006F82BA` → [IopQueueInvalidateBusRelationsRequest + 0x2B](../49/IopQueueInvalidateBusRelationsRequest_function_0049E28C.md) (`tail-transfer`)
  - `0x006F82E4` → [IopQueueInvalidateBusRelationsRequest + 0x2B](../49/IopQueueInvalidateBusRelationsRequest_function_0049E28C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F8228  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
006F822F  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
006F8233  48 85 C9                        test rcx, rcx
006F8236  0F 84 7B 60 DA FF               je 0x14049e2b7
006F823C  BA 88 03 00 00                  mov edx, 0x388
006F8241  48 8D 71 28                     lea rsi, [rcx + 0x28]
006F8245  E8 2A 01 D3 FF                  call 0x140428374
006F824A  66 44 39 3E                     cmp word ptr [rsi], r15w
006F824E  74 16                           je 0x1406f8266
006F8250  8B D7                           mov edx, edi
006F8252  48 8B CE                        mov rcx, rsi
006F8255  E8 1A 01 D3 FF                  call 0x140428374
006F825A  0F B7 16                        movzx edx, word ptr [rsi]
006F825D  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
006F8261  E8 0E 01 D3 FF                  call 0x140428374
006F8266  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
006F826D  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
006F8271  48 83 C1 38                     add rcx, 0x38
006F8275  66 44 39 39                     cmp word ptr [rcx], r15w
006F8279  74 1F                           je 0x1406f829a
006F827B  8B D7                           mov edx, edi
006F827D  E8 F2 00 D3 FF                  call 0x140428374
006F8282  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
006F8289  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
006F828D  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
006F8291  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
006F8295  E8 DA 00 D3 FF                  call 0x140428374
006F829A  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
006F82A1  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
006F82A5  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
006F82A9  48 85 C0                        test rax, rax
006F82AC  0F 84 05 60 DA FF               je 0x14049e2b7
006F82B2  48 8D 48 38                     lea rcx, [rax + 0x38]
006F82B6  66 44 39 39                     cmp word ptr [rcx], r15w
006F82BA  0F 84 F7 5F DA FF               je 0x14049e2b7
006F82C0  8B D7                           mov edx, edi
006F82C2  E8 AD 00 D3 FF                  call 0x140428374
006F82C7  48 8B 83 38 01 00 00            mov rax, qword ptr [rbx + 0x138]
006F82CE  48 8B 48 28                     mov rcx, qword ptr [rax + 0x28]
006F82D2  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
006F82D6  0F B7 51 38                     movzx edx, word ptr [rcx + 0x38]
006F82DA  48 8B 49 40                     mov rcx, qword ptr [rcx + 0x40]
006F82DE  E8 91 00 D3 FF                  call 0x140428374
006F82E3  90                              nop
006F82E4  E9 CE 5F DA FF                  jmp 0x14049e2b7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F8228(void)
{
    __int64 result;

    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40), 904, a3, a4);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40)) != ((unsigned __int16)(v_r15))) {
        a2 = (unsigned int)(v_rdi);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 40 + 8);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40)) + (56);
    result = *(unsigned __int64 *)(v_rbx + 312);
    if ((*(unsigned __int16 *)(a1)) != ((unsigned __int16)(v_r15))) {
        a2 = (unsigned int)(v_rdi);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        result = *(unsigned __int64 *)(v_rbx + 312);
        a1 = *(unsigned __int64 *)(result + 40);
        a2 = *(unsigned __int16 *)(a1 + 56);
        a1 = *(unsigned __int64 *)(a1 + 64);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 16) + 56, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
    result = IoAddTriageDumpDataBlock(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 16) + 64), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 312) + 40) + 16) + 56), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006F8228(void)
{
    int64_t result;

    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28), 904, a3, a4);
    if ((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x28)) != ((uint16_t)(local_r15))) {
        a2 = (uint32_t)(local_rdi);
        a1 = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 40;
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        a2 = *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x28);
        a1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x28 + 0x8);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    a1 = (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28)) + (56);
    result = *(uint64_t *)(local_rbx + 0x138);
    if ((*(uint16_t *)(a1)) != ((uint16_t)(local_r15))) {
        a2 = (uint32_t)(local_rdi);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
        result = *(uint64_t *)(local_rbx + 0x138);
        a1 = *(uint64_t *)(result + 0x28);
        a2 = *(uint16_t *)(a1 + 0x38);
        a1 = *(uint64_t *)(a1 + 0x40);
        result = IoAddTriageDumpDataBlock(a1, a2, a3, a4);
    }
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x10) + 56, (uint32_t)((uint32_t)(local_rdi)), a3, a4);
    result = IoAddTriageDumpDataBlock(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x10) + 0x40), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_rbx + 0x138) + 0x28) + 0x10) + 0x38), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F8228&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F8228[BB_006F8228]
  bb_006F823C[BB_006F823C]
  bb_006F8250[BB_006F8250]
  bb_006F8266[BB_006F8266]
  bb_006F827B[BB_006F827B]
  bb_006F829A[BB_006F829A]
  bb_006F82B2[BB_006F82B2]
  bb_006F82C0[BB_006F82C0]
  bb_006F8228 -->|fallthrough| bb_006F823C
  bb_006F823C -->|branch| bb_006F8266
  bb_006F823C -->|fallthrough| bb_006F8250
  bb_006F8250 -->|flow| bb_006F8266
  bb_006F8266 -->|branch| bb_006F829A
  bb_006F8266 -->|fallthrough| bb_006F827B
  bb_006F827B -->|flow| bb_006F829A
  bb_006F829A -->|fallthrough| bb_006F82B2
  bb_006F82B2 -->|fallthrough| bb_006F82C0
```
