# SymCryptSha1Init

- RVA: `0x00529E70`–`0x00529E92` (길이 `34` bytes)
- VA: `0x0000000140529E70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SymCryptSha1Result](SymCryptSha1Result_function_00529EA0.md) at `0x00529F6D`
- [HashpInitHash](../../page/84/HashpInitHash_function_00842018.md) at `0x00842087`

### Static image references
- `0x00529E7C` → RVA `0x000203D0` (`.rdata`; read)
- `0x00529E87` → RVA `0x000203E0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00529E70  33 C0                           xor eax, eax
00529E72  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
00529E76  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
00529E7A  89 01                           mov dword ptr [rcx], eax
00529E7C  0F 10 05 4D 65 AF FF            movups xmm0, xmmword ptr [rip - 0x509ab3]
00529E83  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00529E87  8B 05 53 65 AF FF               mov eax, dword ptr [rip - 0x509aad]
00529E8D  89 41 70                        mov dword ptr [rcx + 0x70], eax
00529E90  C3                              ret
00529E91  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptSha1Init(__int64 a1)
{
    __int64 result;

    result = 0;
    *(unsigned __int64 *)(a1 + 16) = 0;
    *(unsigned __int64 *)(a1 + 24) = 0;
    *(unsigned int *)(a1) = 0;
    *(unsigned __int64 *)(a1 + 96) = v_xmm0;
    *(unsigned int *)(a1 + 112) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 5282477)));
    return (unsigned int)(*(unsigned int *)(v_rip - 5282477));
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptSha1Init(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    result = 0;
    *(uint64_t *)(arg1 + 0x10) = 0;
    *(uint64_t *)(arg1 + 0x18) = 0;
    *(uint32_t *)(arg1) = 0;
    *(uint64_t *)(arg1 + 0x60) = v_xmm0;
    *(uint32_t *)(arg1 + 0x70) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x509AAD)));
    return (uint32_t)(*(uint32_t *)(v_rip - 0x509AAD));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `W` |
| `Arg1` | `+ 0x60` | `128` | `R` |
| `Arg1` | `+ 0x70` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00529E70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00529E70[BB_00529E70]
  bb_00529E91[BB_00529E91]
```
