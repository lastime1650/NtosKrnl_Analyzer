# sub_008C0FAF

- RVA: `0x008C0FAF`–`0x008C0FCC` (길이 `29` bytes)
- VA: `0x00000001408C0FAF`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083560`
- 디코드: `7`개 명령, `29/29` bytes 표시
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
  - `0x008C0FB8` → [sub_008C0C36 + 0xBC](Unknown_function_008C0C36.md) (`tail-transfer`)
  - `0x008C0FC7` → [sub_008C0C36 + 0xD1](Unknown_function_008C0C36.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C0FAF  8D 82 88 00 00 00               lea eax, [rdx + 0x88]
008C0FB5  89 45 AB                        mov dword ptr [rbp - 0x55], eax
008C0FB8  E9 35 FD FF FF                  jmp 0x1408c0cf2
008C0FBD  33 C0                           xor eax, eax
008C0FBF  44 89 75 17                     mov dword ptr [rbp + 0x17], r14d
008C0FC3  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
008C0FC7  E9 3B FD FF FF                  jmp 0x1408c0d07
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008C0FAF(__int64 a1, __int64 a2)
{
    *(unsigned int *)(v_rbp - 85) = (unsigned int)(a2 + 136);
}
```

## 5. (Beta) C Style

```c
int64_t sub_008C0FAF(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    *(uint32_t *)(local_rbp - 0x55) = (uint32_t)(Arg2 + 136);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x88` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C0FAF&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008C0FAF[BB_008C0FAF]
  bb_008C0FBD[BB_008C0FBD]
```
