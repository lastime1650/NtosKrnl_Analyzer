# sub_00B19096

- RVA: `0x00B19096`–`0x00B190AF` (길이 `25` bytes)
- VA: `0x0000000140B19096`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007CD14`
- 디코드: `7`개 명령, `25/25` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x00B190AA` → [MiInitializePartialVad + 0xE5](../88/MiInitializePartialVad_function_00887954.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B19096  48 8D 45 FF                     lea rax, [rbp - 1]
00B1909A  48 C1 E8 0C                     shr rax, 0xc
00B1909E  89 43 1C                        mov dword ptr [rbx + 0x1c], eax
00B190A1  48 C1 E8 20                     shr rax, 0x20
00B190A5  88 43 21                        mov byte ptr [rbx + 0x21], al
00B190A8  33 FF                           xor edi, edi
00B190AA  E9 8A E9 D6 FF                  jmp 0x140887a39
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B19096(void)
{
    __int64 result;
    __int64 v_rdi;

    result = (v_rbp - 1) >> (12);
    *(unsigned int *)(v_rbx + 28) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned __int8 *)(v_rbx + 33) = (unsigned __int8)(result);
    v_rdi = 0;
}
```

## 5. (Beta) C Style

```c
void sub_00B19096(void)
{
    int64_t result;
    int64_t local_rdi;

    result = (local_rbp - 1) >> (12);
    *(uint32_t *)(local_rbx + 0x1C) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint8_t *)(local_rbx + 0x21) = (uint8_t)(result);
    local_rdi = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B19096&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B19096[BB_00B19096]
```
