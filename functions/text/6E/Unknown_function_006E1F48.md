# sub_006E1F48

- RVA: `0x006E1F48`–`0x006E1F9E` (길이 `86` bytes)
- VA: `0x00000001406E1F48`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00076978`
- 디코드: `24`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006E1F93` → [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) (function, `0x002BA000`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006E1F99` → [sub_0033535B + 0x17E](../33/Unknown_function_0033535B.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E1F48  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
006E1F4C  48 B9 FF FF FF FF FF FF FF BF   movabs rcx, 0xbfffffffffffffff
006E1F56  48 23 C1                        and rax, rcx
006E1F59  BA 00 01 00 00                  mov edx, 0x100
006E1F5E  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
006E1F62  49 8B CE                        mov rcx, r14
006E1F65  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
006E1F69  89 45 70                        mov dword ptr [rbp + 0x70], eax
006E1F6C  C1 E8 10                        shr eax, 0x10
006E1F6F  24 FD                           and al, 0xfd
006E1F71  0C 05                           or al, 5
006E1F73  88 45 72                        mov byte ptr [rbp + 0x72], al
006E1F76  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
006E1F79  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
006E1F7D  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
006E1F81  89 45 70                        mov dword ptr [rbp + 0x70], eax
006E1F84  C1 E8 18                        shr eax, 0x18
006E1F87  0C 10                           or al, 0x10
006E1F89  88 45 73                        mov byte ptr [rbp + 0x73], al
006E1F8C  8B 45 70                        mov eax, dword ptr [rbp + 0x70]
006E1F8F  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
006E1F93  E8 68 80 BD FF                  call 0x1402ba000
006E1F98  90                              nop
006E1F99  E9 3B 35 C5 FF                  jmp 0x1403354d9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E1F48(void)
{
    __int64 result;

    result = (*(unsigned __int64 *)(v_r14 + 24)) & (a1);
    *(unsigned __int64 *)(v_r14 + 24) = result;
    *(unsigned int *)(v_rbp + 112) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (16));
    result = (unsigned __int8)((result) & (253));
    result = (unsigned __int8)((result) | (5));
    *(unsigned __int8 *)(v_rbp + 114) = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 112)));
    *(unsigned int *)(v_rbp + 112) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (24));
    result = (unsigned __int8)((result) | (16));
    *(unsigned __int8 *)(v_rbp + 115) = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp + 112)));
    result = MiInsertPageInList(v_r14, 256, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006E1F48(void)
{
    int64_t result;

    result = (*(uint64_t *)(local_r14 + 0x18)) & (a1);
    *(uint64_t *)(local_r14 + 0x18) = result;
    *(uint32_t *)(local_rbp + 0x70) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (16));
    result = (uint8_t)((result) & (253));
    result = (uint8_t)((result) | (5));
    *(uint8_t *)(local_rbp + 0x72) = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x70)));
    *(uint32_t *)(local_rbp + 0x70) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (24));
    result = (uint8_t)((result) | (16));
    *(uint8_t *)(local_rbp + 0x73) = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp + 0x70)));
    result = MiInsertPageInList(local_r14, 256, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E1F48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E1F48[BB_006E1F48]
```
