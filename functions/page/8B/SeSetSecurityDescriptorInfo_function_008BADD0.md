# SeSetSecurityDescriptorInfo

- RVA: `0x008BADD0`–`0x008BAE0C` (길이 `60` bytes)
- VA: `0x00000001408BADD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082E10`
- 디코드: `17`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008BADFA` → [RtlpSetSecurityObject](RtlpSetSecurityObject_function_008BB500.md) (function, `0x008BB500`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008BADD0  48 83 EC 48                     sub rsp, 0x48
008BADD4  45 33 D2                        xor r10d, r10d
008BADD7  4D 39 11                        cmp qword ptr [r9], r10
008BADDA  74 29                           je 0x1408bae05
008BADDC  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
008BADE1  8B 12                           mov edx, dword ptr [rdx]
008BADE3  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
008BADE8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008BADED  8B 44 24 70                     mov eax, dword ptr [rsp + 0x70]
008BADF1  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008BADF5  44 89 54 24 20                  mov dword ptr [rsp + 0x20], r10d
008BADFA  E8 01 07 00 00                  call 0x1408bb500
008BADFF  48 83 C4 48                     add rsp, 0x48
008BAE03  C3                              ret
008BAE04  CC                              int3
008BAE05  B8 D7 00 00 C0                  mov eax, 0xc00000d7
008BAE0A  EB F3                           jmp 0x1408badff
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeSetSecurityDescriptorInfo(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_r10 = 0;
    if ((*(unsigned __int64 *)(a4)) == 0) goto loc_008BAE05;
    v_stack_m10 = 0;
    v_stack_m18 = a6;
    v_stack_m20 = (unsigned int)((unsigned int)(a5));
    v_stack_m28 = 0;
    result = RtlpSetSecurityObject(a1, (unsigned int)(*(unsigned int *)(a2)), a3, a4);
loc_008BADFF:
    v_rsp = (v_rsp) + (72);
    return result;
loc_008BAE05:
    goto loc_008BADFF;
}
```

## 5. (Beta) C Style

```c
int64_t SeSetSecurityDescriptorInfo(int64_t Arg1, void *Arg2, int64_t Arg3, void *Arg4, uint32_t Arg5, int64_t Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    local_r10 = 0;
    if ((*(uint64_t *)(arg4)) == 0) goto loc_008BAE05;
    v_stack_m10 = 0;
    v_stack_m18 = Arg6;
    v_stack_m20 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m28 = 0;
    result = RtlpSetSecurityObject(Arg1, (uint32_t)(*(uint32_t *)(arg2)), Arg3, Arg4);
loc_008BADFF:
    local_rsp = (local_rsp) + (72);
    return result;
loc_008BAE05:
    goto loc_008BADFF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `32` | `R` |
| `Arg4` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008BADD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008BADD0[BB_008BADD0]
  bb_008BADDC[BB_008BADDC]
  bb_008BADFF[BB_008BADFF]
  bb_008BAE04[BB_008BAE04]
  bb_008BAE05[BB_008BAE05]
  bb_008BADD0 -->|branch| bb_008BAE05
  bb_008BADD0 -->|fallthrough| bb_008BADDC
  bb_008BADDC -->|flow| bb_008BADFF
  bb_008BAE04 -->|flow| bb_008BAE05
  bb_008BAE05 -->|branch| bb_008BADFF
```
