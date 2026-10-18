# AlpcpRemoveMessagePort

- RVA: `0x009F441C`–`0x009F4455` (길이 `57` bytes)
- VA: `0x00000001409F441C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `17`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [AlpcpCancelMessage](../89/AlpcpCancelMessage_function_00894120.md) at `0x008944FE`
- [sub_00B197CC](../B1/Unknown_function_00B197CC.md) at `0x00B199EB`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F441C  8B 42 28                        mov eax, dword ptr [rdx + 0x28]
009F441F  83 E0 07                        and eax, 7
009F4422  83 F8 01                        cmp eax, 1
009F4425  75 26                           jne 0x1409f444d
009F4427  FF 89 C0 01 00 00               dec dword ptr [rcx + 0x1c0]
009F442D  83 62 28 F8                     and dword ptr [rdx + 0x28], 0xfffffff8
009F4431  48 83 62 10 00                  and qword ptr [rdx + 0x10], 0
009F4436  48 8B 4A 08                     mov rcx, qword ptr [rdx + 8]
009F443A  48 8B 02                        mov rax, qword ptr [rdx]
009F443D  48 89 01                        mov qword ptr [rcx], rax
009F4440  48 8B 0A                        mov rcx, qword ptr [rdx]
009F4443  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
009F4447  48 89 41 08                     mov qword ptr [rcx + 8], rax
009F444B  C3                              ret
009F444C  CC                              int3
009F444D  FF 89 C4 01 00 00               dec dword ptr [rcx + 0x1c4]
009F4453  EB D8                           jmp 0x1409f442d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AlpcpRemoveMessagePort(__int64 a1, __int64 a2)
{
    __int64 result;

    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 40))) & (7));
    if (((unsigned int)(result)) != 1) goto loc_009F444D;
loc_009F442D:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8)) = *(unsigned __int64 *)(a2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8) = *(unsigned __int64 *)(a2 + 8);
    return *(unsigned __int64 *)(a2 + 8);
loc_009F444D:
    goto loc_009F442D;
}
```

## 5. (Beta) C Style

```c
int64_t AlpcpRemoveMessagePort(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x28))) & (7));
    if (((uint32_t)(result)) != 1) goto loc_009F444D;
loc_009F442D:
    *(uint64_t *)(*(uint64_t *)(arg2 + 0x8)) = *(uint64_t *)(arg2);
    *(uint64_t *)(*(uint64_t *)(arg2) + 0x8) = *(uint64_t *)(arg2 + 0x8);
    return *(uint64_t *)(arg2 + 0x8);
loc_009F444D:
    goto loc_009F442D;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1C0` | `32` | `R/W` |
| `Arg1` | `+ 0x1C4` | `32` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R/W` |
| `Arg2` | `+ 0x28` | `32` | `R` |
| `Arg2` | `+ 0x28` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F441C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009F441C[BB_009F441C]
  bb_009F4427[BB_009F4427]
  bb_009F442D[BB_009F442D]
  bb_009F444C[BB_009F444C]
  bb_009F444D[BB_009F444D]
  bb_009F441C -->|branch| bb_009F444D
  bb_009F441C -->|fallthrough| bb_009F4427
  bb_009F4427 -->|flow| bb_009F442D
  bb_009F444C -->|flow| bb_009F444D
  bb_009F444D -->|branch| bb_009F442D
```
