# ExpTimerDpcRoutine$fin$2

- RVA: `0x006D439B`–`0x006D43F9` (길이 `94` bytes)
- VA: `0x00000001406D439B`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B5BEC`
- 디코드: `26`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x006D43CA` → [local_unwind](../4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006D43BC` → RVA `0x004A1614` (`.text`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006D439B  40 55                           push rbp
006D439D  48 83 EC 30                     sub rsp, 0x30
006D43A1  48 8B EA                        mov rbp, rdx
006D43A4  88 4D 59                        mov byte ptr [rbp + 0x59], cl
006D43A7  84 C9                           test cl, cl
006D43A9  74 47                           je 0x1406d43f2
006D43AB  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D43AE  83 F8 24                        cmp eax, 0x24
006D43B1  75 1D                           jne 0x1406d43d0
006D43B3  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D43B6  83 C0 09                        add eax, 9
006D43B9  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D43BC  48 8D 15 51 D2 DC FF            lea rdx, [rip - 0x232daf]
006D43C3  48 8B 8D 80 01 00 00            mov rcx, qword ptr [rbp + 0x180]
006D43CA  E8 71 B7 E2 FF                  call 0x1404ffb40
006D43CF  90                              nop
006D43D0  48 83 A5 00 01 00 00 00         and qword ptr [rbp + 0x100], 0
006D43D8  48 8B 8D 61 01 00 00            mov rcx, qword ptr [rbp + 0x161]
006D43DF  48 89 8D 00 01 00 00            mov qword ptr [rbp + 0x100], rcx
006D43E6  48 8B 85 11 01 00 00            mov rax, qword ptr [rbp + 0x111]
006D43ED  48 D3 C8                        ror rax, cl
006D43F0  8B 00                           mov eax, dword ptr [rax]
006D43F2  48 83 C4 30                     add rsp, 0x30
006D43F6  5D                              pop rbp
006D43F7  C3                              ret
006D43F8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTimerDpcRoutine_fin_2(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int8 *)(a2 + 89) = a1;
    if (a1 == 0) goto loc_006D43F2;
    result = (unsigned int)(*(unsigned int *)(a2 + 48));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) == 36) {
        result = *(unsigned int *)(a2 + 48);
        result = (unsigned int)((result) + (9));
        *(unsigned int *)(a2 + 48) = (unsigned int)(result);
        a2 = v_rip - 2305455;
        a1 = *(unsigned __int64 *)(a2 + 384);
        result = local_unwind(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(a2 + 256) = *(unsigned __int64 *)(a2 + 353);
loc_006D43F2:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 273)));
}
```

## 5. (Beta) C Style

```c
int64_t ExpTimerDpcRoutine_fin_2(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    *(uint8_t *)(arg2 + 0x59) = Arg1;
    if (Arg1 == 0) goto loc_006D43F2;
    result = (uint32_t)(*(uint32_t *)(arg2 + 0x30));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) == 36) {
        result = *(uint32_t *)(arg2 + 0x30);
        result = (uint32_t)((result) + (9));
        *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
        Arg2 = v_rip - 2305455;
        Arg1 = *(uint64_t *)(arg2 + 0x180);
        result = local_unwind(Arg1, Arg2, a3, a4);
    }
    *(uint64_t *)(arg2 + 0x100) = *(uint64_t *)(arg2 + 0x161);
loc_006D43F2:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x111)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x59` | `8` | `W` |
| `Arg2` | `+ 0x100` | `64` | `R/W` |
| `Arg2` | `+ 0x100` | `64` | `W` |
| `Arg2` | `+ 0x111` | `64` | `R` |
| `Arg2` | `+ 0x161` | `64` | `R` |
| `Arg2` | `+ 0x180` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D439B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D439B[BB_006D439B]
  bb_006D43AB[BB_006D43AB]
  bb_006D43B3[BB_006D43B3]
  bb_006D43D0[BB_006D43D0]
  bb_006D43F2[BB_006D43F2]
  bb_006D43F8[BB_006D43F8]
  bb_006D439B -->|branch| bb_006D43F2
  bb_006D439B -->|fallthrough| bb_006D43AB
  bb_006D43AB -->|branch| bb_006D43D0
  bb_006D43AB -->|fallthrough| bb_006D43B3
  bb_006D43B3 -->|flow| bb_006D43D0
  bb_006D43D0 -->|flow| bb_006D43F2
```
