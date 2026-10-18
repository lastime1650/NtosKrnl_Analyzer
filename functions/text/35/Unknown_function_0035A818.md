# sub_0035A818

- RVA: `0x0035A818`–`0x0035A838` (길이 `32` bytes)
- VA: `0x000000014035A818`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000799E0`
- 디코드: `7`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0035A82E` → [CcPostDeferredWrites](CcPostDeferredWrites_function_003590FC.md) (function, `0x003590FC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0035A822` → [sub_0035A582 + 0x45](Unknown_function_0035A582.md) (`tail-transfer`)
  - `0x0035A833` → [sub_0035A582 + 0x45](Unknown_function_0035A582.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0035A818  48 8B 81 B8 00 00 00            mov rax, qword ptr [rcx + 0xb8]
0035A81F  48 39 00                        cmp qword ptr [rax], rax
0035A822  0F 84 9F FD FF FF               je 0x14035a5c7
0035A828  48 8B D7                        mov rdx, rdi
0035A82B  49 8B CD                        mov rcx, r13
0035A82E  E8 C9 E8 FF FF                  call 0x1403590fc
0035A833  E9 8F FD FF FF                  jmp 0x14035a5c7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0035A818(__int64 a1)
{
    __int64 result;

    result = CcPostDeferredWrites(v_r13, v_rdi, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_0035A818(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = CcPostDeferredWrites(local_r13, local_rdi, a3, a4);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0035A818&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0035A818[BB_0035A818]
  bb_0035A828[BB_0035A828]
  bb_0035A818 -->|fallthrough| bb_0035A828
```
