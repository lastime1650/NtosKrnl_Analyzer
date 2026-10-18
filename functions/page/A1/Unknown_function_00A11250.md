# sub_00A11250

- RVA: `0x00A11250`–`0x00A11270` (길이 `32` bytes)
- VA: `0x0000000140A11250`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `32/32` bytes 표시
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
00A11250  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00A11255  83 E1 01                        and ecx, 1
00A11258  44 8B 44 24 38                  mov r8d, dword ptr [rsp + 0x38]
00A1125D  44 33 04 8A                     xor r8d, dword ptr [rdx + rcx*4]
00A11261  48 8D 41 FF                     lea rax, [rcx - 1]
00A11265  83 E0 01                        and eax, 1
00A11268  8B 04 82                        mov eax, dword ptr [rdx + rax*4]
00A1126B  41 2B C0                        sub eax, r8d
00A1126E  C3                              ret
00A1126F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00A11250(int a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, unsigned int a7)
{
    __int64 result;

    a1 = (unsigned int)((a1) & (1));
    a3 = (unsigned int)(((unsigned int)(a7)) ^ (*(unsigned int *)(a6 + a1 * 4)));
    result = (unsigned int)((a1 - 1) & (1));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a6 + result * 4))) - ((unsigned int)(a3)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_00A11250(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, void *Arg6, uint32_t Arg7)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;

    Arg1 = (uint32_t)((Arg1) & (1));
    Arg3 = (uint32_t)(((uint32_t)(Arg7)) ^ (*(uint32_t *)(arg6 + arg1 * 4)));
    result = (uint32_t)((Arg1 - 1) & (1));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg6 + result * 4))) - ((uint32_t)(Arg3)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `- 0x1` | `64` | `R` |
| `Arg6` | `+ 0x0 + rax*4` | `32` | `R` |
| `Arg6` | `+ 0x0 + rcx*4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A11250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A11250[BB_00A11250]
  bb_00A1126F[BB_00A1126F]
```
