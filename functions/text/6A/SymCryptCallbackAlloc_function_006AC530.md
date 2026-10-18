# SymCryptCallbackAlloc

- RVA: `0x006AC530`–`0x006AC55F` (길이 `47` bytes)
- VA: `0x00000001406AC530`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006AC53C` → [MincryptAlloc](../../page/83/MincryptAlloc_function_0083A6D8.md) (function, `0x0083A6D8`)

### Direct callers
- [SymCryptRsakeyAllocate](../52/SymCryptRsakeyAllocate_function_00522CF4.md) at `0x00522D11`
- [SymCryptRsakeySetValueInternal](../52/SymCryptRsakeySetValueInternal_function_005238D4.md) at `0x00523C61`
- [SymCryptEcurveAllocate](../52/SymCryptEcurveAllocate_function_00524074.md) at `0x005240BF`
- [SymCryptEcurveAllocate](../52/SymCryptEcurveAllocate_function_00524074.md) at `0x005240D2`
- [SymCryptEckeyAllocate](../52/SymCryptEckeyAllocate_function_00524A0C.md) at `0x00524A29`
- [SymCryptEckeySetValue](../52/SymCryptEckeySetValue_function_00524C34.md) at `0x00524D1C`
- [SymCryptEcDsaSignEx](../52/SymCryptEcDsaSignEx_function_00525D6C.md) at `0x00525EBD`
- [SymCryptEcDsaVerify](../52/SymCryptEcDsaVerify_function_00526400.md) at `0x00526591`
- [SymCryptRsaPkcs1Sign](../52/SymCryptRsaPkcs1Sign_function_005271A0.md) at `0x00527226`
- [SymCryptRsaPkcs1Verify](../52/SymCryptRsaPkcs1Verify_function_005272FC.md) at `0x0052737D`
- [SymCryptRsaSelftest](../52/SymCryptRsaSelftest_function_0052B638.md) at `0x0052B676`
- [SymCryptFdefIntAllocate](../53/SymCryptFdefIntAllocate_function_0053594C.md) at `0x00535975`
- [SymCryptEcDhSecretAgreement](../53/SymCryptEcDhSecretAgreement_function_00537798.md) at `0x00537853`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x006AC53C` → [MincryptAlloc](../../page/83/MincryptAlloc_function_0083A6D8.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AC530  40 53                           push rbx
006AC532  48 83 EC 20                     sub rsp, 0x20
006AC536  48 83 C1 24                     add rcx, 0x24
006AC53A  33 DB                           xor ebx, ebx
006AC53C  E8 97 E1 18 00                  call 0x14083a6d8
006AC541  48 85 C0                        test rax, rax
006AC544  74 0F                           je 0x1406ac555
006AC546  48 8D 58 23                     lea rbx, [rax + 0x23]
006AC54A  48 83 E3 E0                     and rbx, 0xffffffffffffffe0
006AC54E  8B CB                           mov ecx, ebx
006AC550  2B C8                           sub ecx, eax
006AC552  89 4B FC                        mov dword ptr [rbx - 4], ecx
006AC555  48 8B C3                        mov rax, rbx
006AC558  48 83 C4 20                     add rsp, 0x20
006AC55C  5B                              pop rbx
006AC55D  C3                              ret
006AC55E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptCallbackAlloc(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (36);
    v_rbx = 0;
    result = MincryptAlloc(a1, a2, a3, a4);
    if (result != 0) {
        v_rbx = result + 35;
        v_rbx = (v_rbx) & (-32);
        a1 = (unsigned int)(v_rbx);
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
        *(unsigned int *)(v_rbx - 4) = (unsigned int)(a1);
    }
    v_rsp = (v_rsp) + (32);
    return v_rbx;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptCallbackAlloc(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (36);
    local_rbx = 0;
    result = MincryptAlloc(Arg1, a2, a3, a4);
    if (result != 0) {
        local_rbx = result + 35;
        local_rbx = (local_rbx) & (-32);
        Arg1 = (uint32_t)(local_rbx);
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
        *(uint32_t *)(local_rbx - 0x4) = (uint32_t)(Arg1);
    }
    local_rsp = (local_rsp) + (32);
    return local_rbx;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AC530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AC530[BB_006AC530]
  bb_006AC546[BB_006AC546]
  bb_006AC555[BB_006AC555]
  bb_006AC55E[BB_006AC55E]
  bb_006AC530 -->|branch| bb_006AC555
  bb_006AC530 -->|fallthrough| bb_006AC546
  bb_006AC546 -->|flow| bb_006AC555
```
