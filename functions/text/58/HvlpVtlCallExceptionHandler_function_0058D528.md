# HvlpVtlCallExceptionHandler

- RVA: `0x0058D528`–`0x0058D557` (길이 `47` bytes)
- VA: `0x000000014058D528`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000622F0`
- 디코드: `11`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0058D551` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0058D52F` → RVA `0x00026A28` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0058D528  48 83 EC 38                     sub rsp, 0x38
0058D52C  48 63 11                        movsxd rdx, dword ptr [rcx]
0058D52F  48 8D 05 F2 94 A9 FF            lea rax, [rip - 0x566b0e]
0058D536  4C 8B 49 20                     mov r9, qword ptr [rcx + 0x20]
0058D53A  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0058D53E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0058D543  48 8B 41 28                     mov rax, qword ptr [rcx + 0x28]
0058D547  B9 1E 00 00 00                  mov ecx, 0x1e
0058D54C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0058D551  E8 0A 01 F7 FF                  call 0x1404fd660
0058D556  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvlpVtlCallExceptionHandler(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (56);
    v_stack_p8 = v_rip - 5663502;
    v_stack_m18 = *(unsigned __int64 *)(a1 + 40);
    result = KeBugCheckEx(30, (int)(*(unsigned int *)(a1)), *(unsigned __int64 *)(a1 + 16), *(unsigned __int64 *)(a1 + 32));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvlpVtlCallExceptionHandler(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (56);
    v_stack_p8 = v_rip - 5663502;
    v_stack_m18 = *(uint64_t *)(arg1 + 0x28);
    result = KeBugCheckEx(30, (int32_t)(*(uint32_t *)(arg1)), *(uint64_t *)(arg1 + 0x10), *(uint64_t *)(arg1 + 0x20));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0058D528&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0058D528[BB_0058D528]
```
