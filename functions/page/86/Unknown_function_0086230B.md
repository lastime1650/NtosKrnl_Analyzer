# sub_0086230B

- RVA: `0x0086230B`–`0x00862322` (길이 `23` bytes)
- VA: `0x000000014086230B`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B5C0`
- 디코드: `6`개 명령, `23/23` bytes 표시
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
  - `0x0086231D` → [sub_008620F8 + 0xA3](Unknown_function_008620F8.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0086230B  4C 89 30                        mov qword ptr [rax], r14
0086230E  48 89 48 08                     mov qword ptr [rax + 8], rcx
00862312  48 89 01                        mov qword ptr [rcx], rax
00862315  49 89 46 08                     mov qword ptr [r14 + 8], rax
00862319  80 4F 40 01                     or byte ptr [rdi + 0x40], 1
0086231D  E9 79 FE FF FF                  jmp 0x14086219b
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0086230B(__int64 a1)
{
    *(unsigned __int64 *)(result) = v_r14;
    *(unsigned __int64 *)(result + 8) = a1;
    *(unsigned __int64 *)(a1) = result;
    *(unsigned __int64 *)(v_r14 + 8) = result;
}
```

## 5. (Beta) C Style

```c
void sub_0086230B(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint64_t *)(result) = local_r14;
    *(void **)(result + 0x8) = Arg1;
    *(uint64_t *)(arg1) = result;
    *(uint64_t *)(local_r14 + 0x8) = result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086230B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0086230B[BB_0086230B]
```
