# sub_002F7DF3

- RVA: `0x002F7DF3`–`0x002F7E25` (길이 `50` bytes)
- VA: `0x00000001402F7DF3`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00072488`
- 디코드: `16`개 명령, `50/50` bytes 표시
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
  - `0x002F7DF6` → [sub_002F7CFF](Unknown_function_002F7CFF.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
002F7DF3  CC                              int3
002F7DF4  85 C0                           test eax, eax
002F7DF6  0F 84 03 FF FF FF               je 0x1402f7cff
002F7DFC  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
002F7E01  33 C0                           xor eax, eax
002F7E03  89 02                           mov dword ptr [rdx], eax
002F7E05  48 B8 00 00 00 00 00 80 FF FF   movabs rax, 0xffff800000000000
002F7E0F  49 C7 01 FF FF FF FF            mov qword ptr [r9], 0xffffffffffffffff
002F7E16  49 89 00                        mov qword ptr [r8], rax
002F7E19  B0 01                           mov al, 1
002F7E1B  48 83 C4 20                     add rsp, 0x20
002F7E1F  41 5E                           pop r14
002F7E21  5F                              pop rdi
002F7E22  5E                              pop rsi
002F7E23  C3                              ret
002F7E24  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_002F7DF3(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_rsp;

    result = 0;
    *(unsigned int *)(a2) = 0;
    *(unsigned __int64 *)(a4) = -1;
    *(unsigned __int64 *)(a3) = 0;
    v_rsp = (v_rsp) + (32);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t sub_002F7DF3(int64_t Arg1, void *Arg2, void *Arg3, void *Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;

    result = 0;
    *(uint32_t *)(arg2) = 0;
    *(uint64_t *)(arg4) = -1;
    *(uint64_t *)(arg3) = 0;
    local_rsp = (local_rsp) + (32);
    return 1;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F7DF3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F7DF3[BB_002F7DF3]
  bb_002F7DFC[BB_002F7DFC]
  bb_002F7E24[BB_002F7E24]
  bb_002F7DF3 -->|fallthrough| bb_002F7DFC
```
