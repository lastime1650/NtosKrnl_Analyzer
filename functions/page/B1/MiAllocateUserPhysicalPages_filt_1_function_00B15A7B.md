# MiAllocateUserPhysicalPages$filt$1

- RVA: `0x00B15A7B`–`0x00B15AB5` (길이 `58` bytes)
- VA: `0x0000000140B15A7B`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000C5CF8`
- 디코드: `16`개 명령, `58/58` bytes 표시
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
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B15A7B  40 55                           push rbp
00B15A7D  48 83 EC 50                     sub rsp, 0x50
00B15A81  48 8B EA                        mov rbp, rdx
00B15A84  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B15A8D  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
00B15A94  48 8B 85 38 01 00 00            mov rax, qword ptr [rbp + 0x138]
00B15A9B  8A 88 32 02 00 00               mov cl, byte ptr [rax + 0x232]
00B15AA1  88 4D 65                        mov byte ptr [rbp + 0x65], cl
00B15AA4  8A 4D 65                        mov cl, byte ptr [rbp + 0x65]
00B15AA7  33 C0                           xor eax, eax
00B15AA9  84 C9                           test cl, cl
00B15AAB  0F 95 C0                        setne al
00B15AAE  48 83 C4 50                     add rsp, 0x50
00B15AB2  5D                              pop rbp
00B15AB3  C3                              ret
00B15AB4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAllocateUserPhysicalPages_filt_1(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (80);
    *(unsigned __int64 *)(a2 + 312) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned __int8 *)(a2 + 101) = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 312) + 562));
    result = 0;
    result = ((unsigned __int8)(*(unsigned __int8 *)(a2 + 101)) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAllocateUserPhysicalPages_filt_1(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (80);
    *(uint64_t *)(arg2 + 0x138) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint8_t *)(arg2 + 0x65) = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x138) + 0x232));
    result = 0;
    result = ((uint8_t)(*(uint8_t *)(arg2 + 0x65)) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x65` | `8` | `R` |
| `Arg2` | `+ 0x65` | `8` | `W` |
| `Arg2` | `+ 0x138` | `64` | `R` |
| `Arg2` | `+ 0x138` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B15A7B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B15A7B[BB_00B15A7B]
  bb_00B15AB4[BB_00B15AB4]
```
