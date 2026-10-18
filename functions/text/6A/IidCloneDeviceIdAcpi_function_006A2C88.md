# IidCloneDeviceIdAcpi

- RVA: `0x006A2C88`–`0x006A2CC9` (길이 `65` bytes)
- VA: `0x00000001406A2C88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `19`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006A2CBC` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [IidCloneDeviceId](../../page/82/IidCloneDeviceId_function_008289F8.md) at `0x00828A3F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006A2C88  48 83 EC 28                     sub rsp, 0x28
006A2C8C  0F 10 01                        movups xmm0, xmmword ptr [rcx]
006A2C8F  48 8D 42 18                     lea rax, [rdx + 0x18]
006A2C93  49 83 C8 FF                     or r8, 0xffffffffffffffff
006A2C97  0F 11 02                        movups xmmword ptr [rdx], xmm0
006A2C9A  F2 0F 10 49 10                  movsd xmm1, qword ptr [rcx + 0x10]
006A2C9F  F2 0F 11 4A 10                  movsd qword ptr [rdx + 0x10], xmm1
006A2CA4  48 89 42 08                     mov qword ptr [rdx + 8], rax
006A2CA8  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
006A2CAC  49 FF C0                        inc r8
006A2CAF  42 80 3C 02 00                  cmp byte ptr [rdx + r8], 0
006A2CB4  75 F6                           jne 0x1406a2cac
006A2CB6  49 FF C0                        inc r8
006A2CB9  48 8B C8                        mov rcx, rax
006A2CBC  E8 7F 3B 02 00                  call 0x1406c6840
006A2CC1  33 C0                           xor eax, eax
006A2CC3  48 83 C4 28                     add rsp, 0x28
006A2CC7  C3                              ret
006A2CC8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IidCloneDeviceIdAcpi(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = (a3) | (-1);
    *(unsigned __int64 *)(a2) = v_xmm0;
    *(unsigned __int64 *)(a2 + 16) = v_xmm1;
    *(unsigned __int64 *)(a2 + 8) = a2 + 24;
loc_006A2CAC:
    a3 = (a3) + 1;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + a3 * 1)) != 0) goto loc_006A2CAC;
    a3 = (a3) + 1;
    result = memcpy(a2 + 24, *(unsigned __int64 *)(a1 + 8), a3, a4);
    result = 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IidCloneDeviceIdAcpi(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = (Arg3) | (-1);
    *(uint64_t *)(arg2) = v_xmm0;
    *(uint64_t *)(arg2 + 0x10) = v_xmm1;
    *(void **)(arg2 + 0x8) = Arg2 + 24;
loc_006A2CAC:
    Arg3 = (Arg3) + 1;
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + Arg3 * 1)) != 0) goto loc_006A2CAC;
    Arg3 = (Arg3) + 1;
    result = memcpy(Arg2 + 24, *(uint64_t *)(arg1 + 0x8), Arg3, a4);
    result = 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `64` | `W` |
| `Arg2` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006A2C88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006A2C88[BB_006A2C88]
  bb_006A2CAC[BB_006A2CAC]
  bb_006A2CB6[BB_006A2CB6]
  bb_006A2CC8[BB_006A2CC8]
  bb_006A2C88 -->|flow| bb_006A2CAC
  bb_006A2CAC -->|branch| bb_006A2CAC
  bb_006A2CAC -->|fallthrough| bb_006A2CB6
```
