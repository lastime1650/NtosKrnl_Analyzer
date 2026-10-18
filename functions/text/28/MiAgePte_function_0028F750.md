# MiAgePte

- RVA: `0x0028F750`–`0x0028F780` (길이 `48` bytes)
- VA: `0x000000014028F750`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00067310`
- 디코드: `14`개 명령, `48/48` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiWalkPageTablesRecursively](../27/MiWalkPageTablesRecursively_function_002796C0.md) at `0x0027A7EC`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0028F77A` → [sub_0028FA07](Unknown_function_0028FA07.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0028F750  40 57                           push rdi
0028F752  41 54                           push r12
0028F754  41 55                           push r13
0028F756  41 56                           push r14
0028F758  41 57                           push r15
0028F75A  48 83 EC 30                     sub rsp, 0x30
0028F75E  48 8B B9 B8 00 00 00            mov rdi, qword ptr [rcx + 0xb8]
0028F765  45 8B E0                        mov r12d, r8d
0028F768  4C 8B 69 20                     mov r13, qword ptr [rcx + 0x20]
0028F76C  4C 8B F2                        mov r14, rdx
0028F76F  4C 8B F9                        mov r15, rcx
0028F772  80 7F 06 00                     cmp byte ptr [rdi + 6], 0
0028F776  4D 8B 55 10                     mov r10, qword ptr [r13 + 0x10]
0028F77A  0F 85 87 02 00 00               jne 0x14028fa07
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall MiAgePte(__int64 a1, __int64 a2, int a3)
{
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
}
```

## 5. (Beta) C Style

```c
void MiAgePte(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0028F750&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0028F750[BB_0028F750]
```
