# IopBusNumberUnpackRequirement

- RVA: `0x0072F8E0`–`0x0072F902` (길이 `34` bytes)
- VA: `0x000000014072F8E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `34/34` bytes 표시
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
0072F8E0  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
0072F8E3  48 89 02                        mov qword ptr [rdx], rax
0072F8E6  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
0072F8E9  49 89 00                        mov qword ptr [r8], rax
0072F8EC  8B 41 08                        mov eax, dword ptr [rcx + 8]
0072F8EF  49 89 01                        mov qword ptr [r9], rax
0072F8F2  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
0072F8F7  48 C7 00 01 00 00 00            mov qword ptr [rax], 1
0072F8FE  33 C0                           xor eax, eax
0072F900  C3                              ret
0072F901  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopBusNumberUnpackRequirement(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;

    *(unsigned __int64 *)(a2) = (unsigned int)(*(unsigned int *)(a1 + 12));
    *(unsigned __int64 *)(a3) = (unsigned int)(*(unsigned int *)(a1 + 16));
    *(unsigned __int64 *)(a4) = (unsigned int)(*(unsigned int *)(a1 + 8));
    *(unsigned __int64 *)(a5) = 1;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopBusNumberUnpackRequirement(void *Arg1, void *Arg2, void *Arg3, void *Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;

    *(uint64_t *)(arg2) = (uint32_t)(*(uint32_t *)(arg1 + 0xC));
    *(uint64_t *)(arg3) = (uint32_t)(*(uint32_t *)(arg1 + 0x10));
    *(uint64_t *)(arg4) = (uint32_t)(*(uint32_t *)(arg1 + 0x8));
    *(uint64_t *)(arg5) = 1;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg3` | `+ 0x0` | `64` | `W` |
| `Arg4` | `+ 0x0` | `64` | `W` |
| `Arg5` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0072F8E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0072F8E0[BB_0072F8E0]
  bb_0072F901[BB_0072F901]
```
