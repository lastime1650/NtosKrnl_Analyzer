# sub_006EE8FE

- RVA: `0x006EE8FE`–`0x006EE978` (길이 `122` bytes)
- VA: `0x00000001406EE8FE`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A2234`
- 디코드: `30`개 명령, `122/122` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x006EE945` → [MiMakeOutswappedPageResident + 0x124](../43/MiMakeOutswappedPageResident_function_00431AD0.md) (`tail-transfer`)
  - `0x006EE954` → [MiMakeOutswappedPageResident + 0x2FD](../43/MiMakeOutswappedPageResident_function_00431AD0.md) (`tail-transfer`)
  - `0x006EE95D` → [MiMakeOutswappedPageResident + 0x388](../43/MiMakeOutswappedPageResident_function_00431AD0.md) (`tail-transfer`)
  - `0x006EE973` → [MiMakeOutswappedPageResident + 0x1A2](../43/MiMakeOutswappedPageResident_function_00431AD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006EE8FE  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
006EE902  B9 01 00 00 00                  mov ecx, 1
006EE907  89 45 C8                        mov dword ptr [rbp - 0x38], eax
006EE90A  48 BA 01 00 00 00 00 00 00 C0   movabs rdx, 0xc000000000000001
006EE914  66 01 4D C8                     add word ptr [rbp - 0x38], cx
006EE918  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
006EE91B  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
006EE91F  41 8B 46 20                     mov eax, dword ptr [r14 + 0x20]
006EE923  89 45 C8                        mov dword ptr [rbp - 0x38], eax
006EE926  C1 E8 10                        shr eax, 0x10
006EE929  24 FE                           and al, 0xfe
006EE92B  0C 06                           or al, 6
006EE92D  88 45 CA                        mov byte ptr [rbp - 0x36], al
006EE930  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
006EE933  41 89 46 20                     mov dword ptr [r14 + 0x20], eax
006EE937  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
006EE93B  48 23 C2                        and rax, rdx
006EE93E  48 0B C1                        or rax, rcx
006EE941  49 89 46 18                     mov qword ptr [r14 + 0x18], rax
006EE945  E9 AA 32 D4 FF                  jmp 0x140431bf4
006EE94A  48 8B 7D 48                     mov rdi, qword ptr [rbp + 0x48]
006EE94E  41 B9 00 02 00 00               mov r9d, 0x200
006EE954  E9 74 34 D4 FF                  jmp 0x140431dcd
006EE959  F0 48 FF 00                     lock inc qword ptr [rax]
006EE95D  E9 F6 34 D4 FF                  jmp 0x140431e58
006EE962  45 8B E5                        mov r12d, r13d
006EE965  48 89 1F                        mov qword ptr [rdi], rbx
006EE968  41 C1 EC 03                     shr r12d, 3
006EE96C  41 81 E4 FF 01 00 00            and r12d, 0x1ff
006EE973  E9 FA 32 D4 FF                  jmp 0x140431c72
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006EE8FE(void)
{
    __int64 result;

    *(unsigned int *)(v_rbp - 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 56)));
    *(unsigned int *)(v_rbp - 56) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r14 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 32))) >> (16));
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    *(unsigned __int8 *)(v_rbp - 54) = (unsigned __int8)(result);
    *(unsigned int *)(v_r14 + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbp - 56)));
    result = (*(unsigned __int64 *)(v_r14 + 24)) & (a2);
    result = (result) | (1);
    *(unsigned __int64 *)(v_r14 + 24) = result;
}
```

## 5. (Beta) C Style

```c
void sub_006EE8FE(void)
{
    int64_t result;

    *(uint32_t *)(local_rbp - 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x38)));
    *(uint32_t *)(local_rbp - 0x38) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r14 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x20))) >> (16));
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    *(uint8_t *)(local_rbp - 0x36) = (uint8_t)(result);
    *(uint32_t *)(local_r14 + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbp - 0x38)));
    result = (*(uint64_t *)(local_r14 + 0x18)) & (a2);
    result = (result) | (1);
    *(uint64_t *)(local_r14 + 0x18) = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006EE8FE&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006EE8FE[BB_006EE8FE]
  bb_006EE94A[BB_006EE94A]
  bb_006EE959[BB_006EE959]
  bb_006EE962[BB_006EE962]
```
