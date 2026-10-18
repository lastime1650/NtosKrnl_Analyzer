# sub_006F7D8C

- RVA: `0x006F7D8C`–`0x006F7DA2` (길이 `22` bytes)
- VA: `0x00000001406F7D8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B49F4`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F7D8F` → [ZwClose](../6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F7D9D` → [SepReferenceCachedTokenHandles + 0x65](../49/SepReferenceCachedTokenHandles_function_0049BF58.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F7D8C  48 8B 0F                        mov rcx, qword ptr [rdi]
006F7D8F  E8 1C 55 FB FF                  call 0x1406ad2b0
006F7D94  48 8D 7F F8                     lea rdi, [rdi - 8]
006F7D98  83 C3 FF                        add ebx, -1
006F7D9B  75 EF                           jne 0x1406f7d8c
006F7D9D  E9 1B 42 DA FF                  jmp 0x14049bfbd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F7D8C(void)
{
    __int64 result;
    __int64 v_rbx;

    result = ZwClose(*(unsigned __int64 *)(v_rdi), a2, a3, a4);
    v_rbx = (unsigned int)((v_rbx) + (-1));
    if (condition_is_not_equal) goto loc_006F7D8C;
}
```

## 5. (Beta) C Style

```c
void sub_006F7D8C(void)
{
    int64_t result;
    int64_t local_rbx;

    result = ZwClose(*(uint64_t *)(local_rdi), a2, a3, a4);
    local_rbx = (uint32_t)((local_rbx) + (-1));
    if (condition_is_not_equal) goto loc_006F7D8C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F7D8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F7D8C[BB_006F7D8C]
  bb_006F7D9D[BB_006F7D9D]
  bb_006F7D8C -->|branch| bb_006F7D8C
  bb_006F7D8C -->|fallthrough| bb_006F7D9D
```
