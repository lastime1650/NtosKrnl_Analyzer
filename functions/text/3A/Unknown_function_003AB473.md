# sub_003AB473

- RVA: `0x003AB473`–`0x003AB4AF` (길이 `60` bytes)
- VA: `0x00000001403AB473`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008B944`
- 디코드: `15`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003AB487` → [NP_CONTEXT::NpLeafRefInternal](NP_CONTEXT_NpLeafRefInternal_function_003AA340.md) (function, `0x003AA340`)
- `0x003AB4A4` → [NP_CONTEXT::NpLeafDerefInternal](NP_CONTEXT_NpLeafDerefInternal_function_003A9A70.md) (function, `0x003A9A70`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x003AB477` → [sub_003AB41E + 0x2E](Unknown_function_003AB41E.md) (`tail-transfer`)
  - `0x003AB496` → [sub_006E6C8A](../6E/Unknown_function_006E6C8A.md) (`tail-transfer`)
  - `0x003AB4AA` → [sub_006E6C8A](../6E/Unknown_function_006E6C8A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003AB473  80 7B 02 02                     cmp byte ptr [rbx + 2], 2
003AB477  75 D3                           jne 0x1403ab44c
003AB479  41 B8 01 00 00 00               mov r8d, 1
003AB47F  48 8D 53 08                     lea rdx, [rbx + 8]
003AB483  49 8D 4E 10                     lea rcx, [r14 + 0x10]
003AB487  E8 B4 EE FF FF                  call 0x1403aa340
003AB48C  49 89 06                        mov qword ptr [r14], rax
003AB48F  49 8B 46 10                     mov rax, qword ptr [r14 + 0x10]
003AB493  83 38 FF                        cmp dword ptr [rax], -1
003AB496  0F 84 EE B7 33 00               je 0x1406e6c8a
003AB49C  48 8D 53 08                     lea rdx, [rbx + 8]
003AB4A0  49 8D 4E 10                     lea rcx, [r14 + 0x10]
003AB4A4  E8 C7 E5 FF FF                  call 0x1403a9a70
003AB4A9  90                              nop
003AB4AA  E9 DB B7 33 00                  jmp 0x1406e6c8a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003AB473(void)
{
    __int64 result;

    result = NP_CONTEXT__NpLeafRefInternal(v_r14 + 16, v_rbx + 8, 1, a4);
    *(unsigned __int64 *)(v_r14) = result;
    result = NP_CONTEXT__NpLeafDerefInternal(v_r14 + 16, v_rbx + 8, 1, a4);
}
```

## 5. (Beta) C Style

```c
void sub_003AB473(void)
{
    int64_t result;

    result = NP_CONTEXT__NpLeafRefInternal(local_r14 + 16, local_rbx + 8, 1, a4);
    *(uint64_t *)(local_r14) = result;
    result = NP_CONTEXT__NpLeafDerefInternal(local_r14 + 16, local_rbx + 8, 1, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003AB473&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003AB473[BB_003AB473]
  bb_003AB479[BB_003AB479]
  bb_003AB49C[BB_003AB49C]
  bb_003AB473 -->|fallthrough| bb_003AB479
  bb_003AB479 -->|fallthrough| bb_003AB49C
```
