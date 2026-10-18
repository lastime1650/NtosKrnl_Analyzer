# sub_006E3BBC

- RVA: `0x006E3BBC`–`0x006E3BCF` (길이 `19` bytes)
- VA: `0x00000001406E3BBC`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A354`
- 디코드: `5`개 명령, `19/19` bytes 표시
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
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x006E3BC2` → [MiAllocateAccessLog + 0x9E](../36/MiAllocateAccessLog_function_0036B04C.md) (`tail-transfer`)
  - `0x006E3BCA` → [MiAllocateAccessLog + 0x115](../36/MiAllocateAccessLog_function_0036B04C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006E3BBC  48 D1 EB                        shr rbx, 1
006E3BBF  49 3B DC                        cmp rbx, r12
006E3BC2  0F 83 22 75 C8 FF               jae 0x14036b0ea
006E3BC8  33 C0                           xor eax, eax
006E3BCA  E9 92 75 C8 FF                  jmp 0x14036b161
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006E3BBC(void)
{
    __int64 result;
    __int64 v_rbx;

    v_rbx = (v_rbx) >> (1);
    result = 0;
}
```

## 5. (Beta) C Style

```c
void sub_006E3BBC(void)
{
    int64_t result;
    int64_t local_rbx;

    local_rbx = (local_rbx) >> (1);
    result = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006E3BBC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006E3BBC[BB_006E3BBC]
  bb_006E3BC8[BB_006E3BC8]
  bb_006E3BBC -->|fallthrough| bb_006E3BC8
```
