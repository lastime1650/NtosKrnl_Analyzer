# ExpTimerDpcRoutine$fin$0

- RVA: `0x006D3F35`–`0x006D3F95` (길이 `96` bytes)
- VA: `0x00000001406D3F35`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B5BD4`
- 디코드: `27`개 명령, `96/96` bytes 표시
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
006D3F35  40 55                           push rbp
006D3F37  48 83 EC 30                     sub rsp, 0x30
006D3F3B  48 8B EA                        mov rbp, rdx
006D3F3E  88 4D 58                        mov byte ptr [rbp + 0x58], cl
006D3F41  84 C9                           test cl, cl
006D3F43  74 49                           je 0x1406d3f8e
006D3F45  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D3F48  83 F8 09                        cmp eax, 9
006D3F4B  8B 45 30                        mov eax, dword ptr [rbp + 0x30]
006D3F4E  75 38                           jne 0x1406d3f88
006D3F50  83 C0 09                        add eax, 9
006D3F53  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D3F56  48 8D 85 61 01 00 00            lea rax, [rbp + 0x161]
006D3F5D  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
006D3F64  48 83 A5 F8 00 00 00 00         and qword ptr [rbp + 0xf8], 0
006D3F6C  48 8B 8D 61 01 00 00            mov rcx, qword ptr [rbp + 0x161]
006D3F73  48 89 8D F8 00 00 00            mov qword ptr [rbp + 0xf8], rcx
006D3F7A  48 8B 85 11 01 00 00            mov rax, qword ptr [rbp + 0x111]
006D3F81  48 D3 C8                        ror rax, cl
006D3F84  8B 00                           mov eax, dword ptr [rax]
006D3F86  EB 06                           jmp 0x1406d3f8e
006D3F88  83 C0 0C                        add eax, 0xc
006D3F8B  89 45 30                        mov dword ptr [rbp + 0x30], eax
006D3F8E  48 83 C4 30                     add rsp, 0x30
006D3F92  5D                              pop rbp
006D3F93  C3                              ret
006D3F94  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpTimerDpcRoutine_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int8 *)(a2 + 88) = a1;
    if (a1 == 0) goto loc_006D3F8E;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a2 + 48)))) != 9) goto loc_006D3F88;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 48))) + (9));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
    *(unsigned __int64 *)(a2 + 176) = a2 + 353;
    *(unsigned __int64 *)(a2 + 248) = *(unsigned __int64 *)(a2 + 353);
    goto loc_006D3F8E;
loc_006D3F88:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 273)))) + (12));
    *(unsigned int *)(a2 + 48) = (unsigned int)(result);
loc_006D3F8E:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpTimerDpcRoutine_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (48);
    *(uint8_t *)(arg2 + 0x58) = Arg1;
    if (Arg1 == 0) goto loc_006D3F8E;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x30)))) != 9) goto loc_006D3F88;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x30))) + (9));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
    *(void **)(arg2 + 0xB0) = Arg2 + 353;
    *(uint64_t *)(arg2 + 0xF8) = *(uint64_t *)(arg2 + 0x161);
    goto loc_006D3F8E;
loc_006D3F88:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x111)))) + (12));
    *(uint32_t *)(arg2 + 0x30) = (uint32_t)(result);
loc_006D3F8E:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `32` | `R` |
| `Arg2` | `+ 0x30` | `32` | `W` |
| `Arg2` | `+ 0x58` | `8` | `W` |
| `Arg2` | `+ 0xB0` | `64` | `W` |
| `Arg2` | `+ 0xF8` | `64` | `R/W` |
| `Arg2` | `+ 0xF8` | `64` | `W` |
| `Arg2` | `+ 0x111` | `64` | `R` |
| `Arg2` | `+ 0x161` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006D3F35&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006D3F35[BB_006D3F35]
  bb_006D3F45[BB_006D3F45]
  bb_006D3F50[BB_006D3F50]
  bb_006D3F88[BB_006D3F88]
  bb_006D3F8E[BB_006D3F8E]
  bb_006D3F94[BB_006D3F94]
  bb_006D3F35 -->|branch| bb_006D3F8E
  bb_006D3F35 -->|fallthrough| bb_006D3F45
  bb_006D3F45 -->|branch| bb_006D3F88
  bb_006D3F45 -->|fallthrough| bb_006D3F50
  bb_006D3F50 -->|branch| bb_006D3F8E
  bb_006D3F88 -->|flow| bb_006D3F8E
```
