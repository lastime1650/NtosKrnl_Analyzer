# RtlpFcCreateAndAddFeatureFromUpdate

- RVA: `0x0079A688`–`0x0079A6EB` (길이 `99` bytes)
- VA: `0x000000014079A688`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `34`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0079A697` → [RtlpFcIsUpdateModifyingOrAddingFeature](RtlpFcIsUpdateModifyingOrAddingFeature_function_0079A9DC.md) (function, `0x0079A9DC`)
- `0x0079A6C6` → [RtlpFcUpdateFeature](RtlpFcUpdateFeature_function_0079AAAC.md) (function, `0x0079AAAC`)
- `0x0079A6D1` → [RtlpFcDoesFeatureHaveUniqueState](RtlpFcDoesFeatureHaveUniqueState_function_0079A6F4.md) (function, `0x0079A6F4`)

### Direct callers
- [RtlpFcUpdateFeatureConfiguration](../AB/RtlpFcUpdateFeatureConfiguration_function_00ABD7A0.md) at `0x00ABD92B`
- [RtlpFcUpdateFeatureConfiguration](../AB/RtlpFcUpdateFeatureConfiguration_function_00ABD7A0.md) at `0x00ABD9B8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0079A688  40 53                           push rbx
0079A68A  48 83 EC 20                     sub rsp, 0x20
0079A68E  4D 8B D8                        mov r11, r8
0079A691  48 8B DA                        mov rbx, rdx
0079A694  4C 8B C9                        mov r9, rcx
0079A697  E8 40 03 00 00                  call 0x14079a9dc
0079A69C  84 C0                           test al, al
0079A69E  74 44                           je 0x14079a6e4
0079A6A0  48 8B 0B                        mov rcx, qword ptr [rbx]
0079A6A3  0F 57 C0                        xorps xmm0, xmm0
0079A6A6  0F 11 01                        movups xmmword ptr [rcx], xmm0
0079A6A9  41 8B 01                        mov eax, dword ptr [r9]
0079A6AC  89 01                           mov dword ptr [rcx], eax
0079A6AE  8B 41 04                        mov eax, dword ptr [rcx + 4]
0079A6B1  8B D0                           mov edx, eax
0079A6B3  41 33 51 04                     xor edx, dword ptr [r9 + 4]
0079A6B7  83 E2 0F                        and edx, 0xf
0079A6BA  33 D0                           xor edx, eax
0079A6BC  0F BA F2 07                     btr edx, 7
0079A6C0  89 51 04                        mov dword ptr [rcx + 4], edx
0079A6C3  49 8B D1                        mov rdx, r9
0079A6C6  E8 E1 03 00 00                  call 0x14079aaac
0079A6CB  4C 8B 03                        mov r8, qword ptr [rbx]
0079A6CE  49 8B C8                        mov rcx, r8
0079A6D1  E8 1E 00 00 00                  call 0x14079a6f4
0079A6D6  84 C0                           test al, al
0079A6D8  74 0A                           je 0x14079a6e4
0079A6DA  41 FF 03                        inc dword ptr [r11]
0079A6DD  49 8D 40 10                     lea rax, [r8 + 0x10]
0079A6E1  48 89 03                        mov qword ptr [rbx], rax
0079A6E4  48 83 C4 20                     add rsp, 0x20
0079A6E8  5B                              pop rbx
0079A6E9  C3                              ret
0079A6EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpFcCreateAndAddFeatureFromUpdate(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = RtlpFcIsUpdateModifyingOrAddingFeature(a1, a2, a3, a1);
    if ((unsigned __int8)(result) == 0) goto loc_0079A6E4;
    *(unsigned __int64 *)(*(unsigned __int64 *)(a2)) = v_xmm0;
    *(unsigned int *)(*(unsigned __int64 *)(a2)) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 4))))) ^ (*(unsigned int *)(a1 + 4)));
    a2 = (unsigned int)((a2) & (15));
    a2 = (unsigned int)((a2) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 4)))));
    *(unsigned int *)(*(unsigned __int64 *)(a2) + 4) = (unsigned int)(a2);
    result = RtlpFcUpdateFeature(*(unsigned __int64 *)(a2), a1, a3, a1);
    result = RtlpFcDoesFeatureHaveUniqueState(*(unsigned __int64 *)(a2), a1, *(unsigned __int64 *)(a2), a1);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(a2) + 16;
        *(unsigned __int64 *)(a2) = result;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpFcCreateAndAddFeatureFromUpdate(int64_t Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = RtlpFcIsUpdateModifyingOrAddingFeature(Arg1, Arg2, Arg3, Arg1);
    if ((uint8_t)(result) == 0) goto loc_0079A6E4;
    *(uint64_t *)(*(uint64_t *)(arg2)) = v_xmm0;
    *(uint32_t *)(*(uint64_t *)(arg2)) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x4))))) ^ (*(uint32_t *)(Arg1 + 0x4)));
    Arg2 = (uint32_t)((Arg2) & (15));
    Arg2 = (uint32_t)((Arg2) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x4)))));
    *(uint32_t *)(*(uint64_t *)(arg2) + 0x4) = (uint32_t)(Arg2);
    result = RtlpFcUpdateFeature(*(uint64_t *)(arg2), Arg1, Arg3, Arg1);
    result = RtlpFcDoesFeatureHaveUniqueState(*(uint64_t *)(arg2), Arg1, *(uint64_t *)(arg2), Arg1);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(arg2) + 16;
        *(uint64_t *)(arg2) = result;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0079A688&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0079A688[BB_0079A688]
  bb_0079A6A0[BB_0079A6A0]
  bb_0079A6DA[BB_0079A6DA]
  bb_0079A6E4[BB_0079A6E4]
  bb_0079A6EA[BB_0079A6EA]
  bb_0079A688 -->|branch| bb_0079A6E4
  bb_0079A688 -->|fallthrough| bb_0079A6A0
  bb_0079A6A0 -->|branch| bb_0079A6E4
  bb_0079A6A0 -->|fallthrough| bb_0079A6DA
  bb_0079A6DA -->|flow| bb_0079A6E4
```
