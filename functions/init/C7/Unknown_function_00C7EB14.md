# sub_00C7EB14

- RVA: `0x00C7EB14`–`0x00C7EB3D` (길이 `41` bytes)
- VA: `0x0000000140C7EB14`
- 실행 섹션: `INIT`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000C2D90`
- 디코드: `12`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C7EB30` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C7EB22` → RVA `0x00BEF284` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C7EB30` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C7EB14  40 55                           push rbp
00C7EB16  48 83 EC 30                     sub rsp, 0x30
00C7EB1A  48 8B EA                        mov rbp, rdx
00C7EB1D  48 89 6C 24 48                  mov qword ptr [rsp + 0x48], rbp
00C7EB22  48 8D 15 5B 07 F7 FF            lea rdx, [rip - 0x8f8a5]
00C7EB29  48 8B 8D C8 00 00 00            mov rcx, qword ptr [rbp + 0xc8]
00C7EB30  E8 0B 10 88 FF                  call 0x1404ffb40
00C7EB35  90                              nop
00C7EB36  48 83 C4 30                     add rsp, 0x30
00C7EB3A  5D                              pop rbp
00C7EB3B  C3                              ret
00C7EB3C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00C7EB14(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (48);
    v_stack_p10 = a2;
    result = local_unwind(*(unsigned __int64 *)(a2 + 200), v_rip - 587941, a3, a4);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00C7EB14(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (48);
    v_stack_p10 = Arg2;
    result = local_unwind(*(uint64_t *)(arg2 + 0xC8), v_rip - 587941, a3, a4);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0xC8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7EB14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C7EB14[BB_00C7EB14]
  bb_00C7EB3C[BB_00C7EB3C]
```
