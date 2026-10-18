# sub_0043E18C

- RVA: `0x0043E18C`–`0x0043E1A6` (길이 `26` bytes)
- VA: `0x000000014043E18C`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A4A78`
- 디코드: `6`개 명령, `26/26` bytes 표시
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
  - `0x0043E19D` → [sub_0043E1ED](Unknown_function_0043E1ED.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0043E18C  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
0043E191  8B 99 B4 00 00 00               mov ebx, dword ptr [rcx + 0xb4]
0043E197  45 8B D0                        mov r10d, r8d
0043E19A  83 FB 02                        cmp ebx, 2
0043E19D  72 4E                           jb 0x14043e1ed
0043E19F  48 8D 91 F8 01 00 00            lea rdx, [rcx + 0x1f8]
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0043E18C(__int64 a1, __int64 a2, int a3)
{
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    return;
}
```

## 5. (Beta) C Style

```c
void sub_0043E18C(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    return;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB4` | `32` | `R` |
| `Arg1` | `+ 0x1F8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0043E18C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0043E18C[BB_0043E18C]
  bb_0043E19F[BB_0043E19F]
  bb_0043E18C -->|fallthrough| bb_0043E19F
```
