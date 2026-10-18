# sub_0042AC9A

- RVA: `0x0042AC9A`–`0x0042ACC7` (길이 `45` bytes)
- VA: `0x000000014042AC9A`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A1268`
- 디코드: `14`개 명령, `45/45` bytes 표시
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
  - `0x0042ACB1` → [sub_0042ACFF](Unknown_function_0042ACFF.md) (`tail-transfer`)
  - `0x0042ACC5` → [sub_0042ACC7 + 0x2C](Unknown_function_0042ACC7.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0042AC9A  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
0042AC9F  48 8B F9                        mov rdi, rcx
0042ACA2  8B 59 40                        mov ebx, dword ptr [rcx + 0x40]
0042ACA5  83 E3 FD                        and ebx, 0xfffffffd
0042ACA8  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
0042ACAD  8B EA                           mov ebp, edx
0042ACAF  85 D2                           test edx, edx
0042ACB1  74 4C                           je 0x14042acff
0042ACB3  40 B6 11                        mov sil, 0x11
0042ACB6  89 5F 40                        mov dword ptr [rdi + 0x40], ebx
0042ACB9  85 ED                           test ebp, ebp
0042ACBB  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0042ACC0  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0042ACC5  75 2C                           jne 0x14042acf3
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_0042AC9A(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 v_rbx;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;

    v_stack_p30 = v_rbx;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 64))) & (0xFFFFFFFDULL));
    v_stack_p38 = v_rbp;
    *(unsigned int *)(a1 + 64) = (unsigned int)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void sub_0042AC9A(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rbx;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;

    v_stack_p30 = local_rbx;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x40))) & (0xFFFFFFFDULL));
    v_stack_p38 = local_rbp;
    *(uint32_t *)(arg1 + 0x40) = (uint32_t)(local_rbx);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x40` | `32` | `R` |
| `Arg1` | `+ 0x40` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0042AC9A&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0042AC9A[BB_0042AC9A]
  bb_0042ACB3[BB_0042ACB3]
  bb_0042AC9A -->|fallthrough| bb_0042ACB3
```
