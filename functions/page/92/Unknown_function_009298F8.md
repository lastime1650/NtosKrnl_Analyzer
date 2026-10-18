# sub_009298F8

- RVA: `0x009298F8`–`0x0092991F` (길이 `39` bytes)
- VA: `0x00000001409298F8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008D8EC`
- 디코드: `11`개 명령, `39/39` bytes 표시
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
  - `0x00929903` → [sub_00929936](Unknown_function_00929936.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009298F8  48 89 6C 24 30                  mov qword ptr [rsp + 0x30], rbp
009298FD  0F B6 29                        movzx ebp, byte ptr [rcx]
00929900  83 FA 04                        cmp edx, 4
00929903  76 31                           jbe 0x140929936
00929905  B8 59 00 00 C0                  mov eax, 0xc0000059
0092990A  48 8B 6C 24 30                  mov rbp, qword ptr [rsp + 0x30]
0092990F  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00929914  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00929919  48 83 C4 20                     add rsp, 0x20
0092991D  5F                              pop rdi
0092991E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_009298F8(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;

    v_stack_p30 = v_rbp;
    v_rsp = (v_rsp) + (32);
    return (unsigned int)(0xC0000059ULL);
}
```

## 5. (Beta) C Style

```c
int64_t sub_009298F8(void *Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, uint64_t Arg7, int64_t Arg8, int64_t Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rsp;
    uint64_t v_stack_p30;

    v_stack_p30 = local_rbp;
    local_rsp = (local_rsp) + (32);
    return (uint32_t)(0xC0000059ULL);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009298F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009298F8[BB_009298F8]
  bb_00929905[BB_00929905]
  bb_009298F8 -->|fallthrough| bb_00929905
```
